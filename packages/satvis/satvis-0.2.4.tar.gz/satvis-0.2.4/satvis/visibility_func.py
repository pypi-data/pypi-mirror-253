"""Calculate visibility between two points near a spherical body.

[1] J. A. Lawton, “Numerical method for rapidly determining satellite-satellite
and satellite-ground station in-view periods,” Journal of Guidance, Control, and
Dynamics, vol. 10, no. 1, pp. 32–36, Jan. 1987, doi: 10.2514/3.20177.
"""
# %% Imports
from __future__ import annotations

# Standard Library Imports
from typing import Tuple
from warnings import warn

# Third Party Imports
from intervaltree import Interval, IntervalTree
from numpy import (
    append,
    arange,
    arccos,
    array,
    atleast_2d,
    dot,
    float32,
    isreal,
    logical_and,
    nan,
    ndarray,
    sign,
    sin,
    where,
)
from numpy.linalg import norm
from numpy.polynomial import Polynomial


# %% Visibility function
def visibilityFunc(
    r1: ndarray,
    r2: ndarray,
    RE: float,
    hg: float,
    tol: float = 1e-13,
) -> Tuple[float, float, float, float]:
    """Calculate visibility function for two position vectors.

    Args:
        r1 (ndarray): [3 X 1] ECI position vector of object 1
        r2 (ndarray): [3 X 1] ECI position vector of object 2
        RE (float): Radius of planet
        hg (float): extra height restriction above planet surface
        tol (float, optional): Tolerance for numerical errors. Defaults to 1e-13.

    Returns:
        v (float): value of visibility function (positive indicates objects
            can see each other). Returns nan if either r1 or r1 are below
            surface of planet.
        phi (float): angle between position vectors
        alpha1 (float): Construction angle 1. Returns numpy.nan if either r1
            or r2 are below surface of planet.
        alpha2 (float): Construction angle 2. Returns numpy.nan if either r1
            or r2 are below surface of planet.

    From "Numerical Method for Rapidly Determining Satellite-Satellite
        and Satellite-Ground Station In-View Periods", by Lawton, 1987.
        All argument units are arbitrary distances, just keep consistent.
    """
    # %% Params
    # small value for error threshold
    eps = tol

    # get magnitude of position vectors and radius of body
    RE_prime = RE + hg
    r1_mag = norm(r1)
    r2_mag = norm(r2)

    # %% Correct magnitudes if needed.
    # if points are slightly below Earth surface, change to be on surface.
    if (RE_prime / r1_mag > 1) and (RE_prime / r1_mag < 1 + eps):
        warn("r1_mag nudged to equal RE_prime")
        r1_mag = RE_prime

    if (RE_prime / r2_mag > 1) and (RE_prime / r2_mag < 1 + eps):
        warn("r2_mag nudged to equal RE_prime")
        r2_mag = RE_prime

    # %% Calculate angle between position vectors
    # Check if numerics cause test_var to be >1, and correct if needed
    # Corrects for issues when vectors are close to each other
    test_var = dot(r1.squeeze(), r2.squeeze()) / (r1_mag * r2_mag)
    if test_var > (1 + eps):
        print(f"dot(r1, r2)/(r1_mag * r2_mag)={dot(r1, r2)/(r1_mag * r2_mag)}")
        raise ValueError("dot(r1, r2)/(r1_mag * r2_mag) > 1")
    elif test_var < (-1 - eps):
        print(f"dot(r1, r2)/(r1_mag * r2_mag)={dot(r1, r2)/(r1_mag * r2_mag)}")
        raise ValueError("dot(r1, r2)/(r1_mag * r2_mag) < -1")
    elif test_var > 1 and test_var < (1 + eps):
        test_var = 1
    elif test_var < -1 and test_var > (-1 - eps):
        test_var = -1

    # angle between vectors
    phi = arccos(test_var)

    # %% If either point is far below  surface of body, abort and report not visible
    # check if points are far below surface of body
    r1_flag = False
    if RE_prime / r1_mag > (1 + eps):
        r1_flag = True
        warn("RE_prime > r1_mag")

    r2_flag = False
    if RE_prime / r2_mag > (1 + eps):
        r2_flag = True
        warn("RE_prime > r2_mag")

    # If either point is far below surface, v and alphas are undefined; return nan.
    if r1_flag or r2_flag:
        v = nan
        alpha1 = nan
        alpha2 = nan
    else:
        # Nominal path, both points are >= body radius.
        # Calc construction angles.
        alpha1 = arccos(RE_prime / r1_mag)
        alpha2 = arccos(RE_prime / r2_mag)
        v = alpha1 + alpha2 - phi

    return v, phi, alpha1, alpha2


# %% Calculate visibility windows
def zeroCrossingFit(
    v: ndarray,
    t: ndarray,
    id: object = None,
) -> Tuple[ndarray[float], ndarray[int], IntervalTree]:
    """Interpolates visibility windows from sparse visibility data.

        Fit curves around zero-crossings of visibility function.
        Fit cubic polynomials to every 4 points, so loop through t[3] - t[end].
        Outputs interval tree object of visibility windows.

        Based on: Alfano, Salvatore, Negron, David Jr., Moore, Jennifer L.,
        “Rapid Determination of Satellite Visibility Periods,” Journal of
        Astronautical Sciences, Vol. 40, No. 2, 1992
    Args:
        v (ndarray): [1 x N] array of floats
        t (ndarray): [1 x N] array of floats
        id (any): (Optional) Identifier for interval tree

    Returns:
        crossings (ndarray[float]): [1 x M] array of times at which the
            visibility function crosses 0
        riseSet (ndarray[int]): [1 x M] array of +-1 indicating if associated
            value in crossings is a rise point (+1) or set point (-1)
        tree (IntervalTree): Interval tree object of time bounds during
            which visibility function is >1

    Note that the ability to detect rise/set times within the first 2 steps
        of the beginning or end of t is sketchy due to the 4-point curve
        fit requirement. Workaround is in-place that does a 1st-order polyfit
        when t[0] and t[1] straddle v=0.
    """
    # initialize
    crossings = array([], dtype=float32)
    riseSet = array([], dtype=int)
    tree = IntervalTree()
    crossIndx = -1

    # Special case: no-zero crossings, V is positive for all time
    if all(sign(v) == 1):
        temp = Interval(t[0], t[-1], id)
        tree.add(temp)
        # print('special case: visible for whole time vector')
        return crossings, riseSet, tree
    # special case: no-zero crossings, V is negative for all time
    elif all(sign(v) == -1):
        # Note: IntervalTree object does not allow null (empty) intervals
        # print('special case: no visibility windows')
        return crossings, riseSet, tree

    # special case: zero-crossing occurs between t[0] and t[1]
    # 1st-order polyfit exception.
    if sign(v[0]) != sign(v[1]):
        crossings = append(crossings, findCrossing(t[:2], v[:2], 1))
        crossIndx += 1
        riseSet = append(riseSet, riseOrSet(v[1]))
        if riseSet[0] == -1:
            temp = Interval(t[0], crossings[0], id)
            tree.add(temp)

    # iterate through time vector for all other cases
    for i in arange(3, len(t)):
        # print('i =' + str(i))
        if i == 3:
            #  starting visibility sign (+1 or -1)
            startV = sign(v[1])

        # print('i =' + str(i))
        # grab 4 time values
        tSnapshot = array([t[i - 3], t[i - 2], t[i - 1], t[i]])
        # grab 4 v values
        vSnapshot = array([v[i - 3], v[i - 2], v[i - 1], v[i]])

        # fit with 2 mid-points on either side of zero
        # if sign(v[i - 1]) != sign(v[i - 2]):
        if sign(vSnapshot[1]) != sign(vSnapshot[2]):
            crossIndx += 1

            # Get new crossing.
            new_crossings = findCrossing(tSnapshot, vSnapshot, 3)
            single_crossing = trimCrossings(new_crossings, tSnapshot)
            crossings = append(crossings, single_crossing)

            # determine if zero-crossing was a rise or set time and assign
            # val to vector
            riseSet = append(riseSet, riseOrSet(v[i - 1]))

            # Construct interval tree for times when v > 0 (visibility
            # windows)
            # wait for 2 crossings to appear, where 2nd crossing is a
            # set time
            if len(crossings) > 1 and sign(riseSet[crossIndx]) == -1:
                temp = Interval(crossings[crossIndx - 1], crossings[crossIndx], id)
                tree.add(temp)
            # create interval if satellite starts in visibility window
            elif len(crossings) == 1 and startV == 1:
                temp = Interval(t[0], crossings[crossIndx], id)
                tree.add(temp)
                # print('special case: first visibility window start
                #        at t0')

        # create interval if simulation ends while visible
        if i == len(t) - 1:
            # at least one crossing has occurred
            if crossIndx >= 0 and sign(v[i]) == 1:
                temp = Interval(crossings[crossIndx], t[i], id)
                tree.add(temp)

    return crossings, riseSet, tree


def trimCrossings(crossings: ndarray, time_snapshot: ndarray) -> ndarray:
    """Trim extra (false) crossings from array.

    Args:
        crossings (ndarray): An array of crossing times.
        time_snapshot (ndarray): A 4-element array of times encompassing crossings
            (i.e. min(time_snapshot) < min(crossings) and
            max(time_snapshot) > max(crossings)).

    Returns:
        ndarray: A single time from crossing that is in between time_snapshot[1]
            and time_snapshot[2].
    """
    assert len(time_snapshot) == 4

    # Get new crossing; grab single element from new_crossings in case
    # multiple crossings are returned.
    if len(crossings) == 1:
        # Single crossing detected, return input
        c = crossings[0]
    else:
        # c = crossings[1]
        lower_bound = time_snapshot[1]
        upper_bound = time_snapshot[2]
        indx = where(logical_and(crossings <= upper_bound, crossings >= lower_bound))
        assert len(indx) == 1
        c = crossings[indx]

    return c


def findCrossing(
    t: ndarray,
    v: ndarray,
    order: int,
) -> ndarray[float]:
    """Fits a N-order polynomial to 4 points and finds root.

    Args:
        t (ndarray): [4,] Time values.
        v (ndarray): [4,] Visibility function values.
        order (int): Order of polyfit.

    Returns:
        ndarray[float]: [1, ] Time of zero-crossing.
    """
    # fit a 3rd-order polynomial
    poly = Polynomial.fit(t, v, order)
    # find roots of polynomial
    polyRoots = poly.roots()
    # discard complex roots
    realRoots = polyRoots[isreal(polyRoots)].real

    # get roots that are in domain (range) of the
    # polynomial (t[i-3] and t[i])
    # values of t where 0-crossings occurred
    inRangeRoots = realRoots[
        (realRoots < poly.domain[1]) & (realRoots > poly.domain[0])
    ]

    return inRangeRoots


def riseOrSet(v_i: float) -> int:
    """Switch case for visibility value.

    Args:
        v_i (float): Value of visibility function

    Returns:
        int: 1, -1, or 0 for rise, set, or anomaly, respectively.
    """
    if sign(v_i) == 1:
        # rise time
        riseSet = 1
    elif sign(v_i) == -1:
        # set time
        riseSet = -1
    else:
        riseSet = 0  # anomaly-->bad!

    return riseSet


def isVis(
    r1: ndarray,
    r2: ndarray,
    RE: float,
    hg: float = 0,
) -> bool:
    """Shortcut wrapper to for boolean visibility.

    Args:
        r1 (ndarray): [3 X 1] ECI position vector of object 1
        r2 (ndarray): [3 X 1] ECI position vector of object 2
        RE (float): Radius of planet
        hg (float): extra height restriction above planet surface

    Returns:
        bool: True if r1 and r2 are visible to each other.
    """
    v, _, _, _ = visibilityFunc(r1, r2, RE, hg)

    # convert to regular bool from numpy.bool
    return bool(v > 0)


def visDerivative(
    r1: ndarray,
    r1dot: ndarray,
    r1mag_dot: float,
    r2: ndarray,
    r2dot: ndarray,
    r2mag_dot: float,
    a1: float,
    a2: float,
    phi: float,
    RE: float,
    hg: float = 0,
    debug: bool = False,
) -> float:
    """Calculate derivative of visibility function.

    Be careful to use the time derivative of the magnitude of the position for
    r#mag_dot. Do not use the magnitude of the velocity vector (r#dot).

    Eq. 2 from [1].

    Args:
        r1 (ndarray): [3 X 1] ECI position vector of the first object.
        r1dot (ndarray): [3 X 1] ECI velocity vector of the first object.
        r1mag_dot (float): Time derivative of the magnitude of the first object's
            position vector.
        r2 (ndarray): [3 X 1] ECI position vector of the second object.
        r2dot (ndarray): [3 X 1] ECI velocity vector of the second object.
        r2mag_dot (float): Time derivative of the magnitude of the second object's
            position vector.
        a1 (float): Construction angle 1 in radians.
        a2 (float): Construction angle 2 in radians.
        phi (float): Angle in radians between the position vectors of the two objects.
        RE (float): Radius of the Earth (or other celestial body).
        hg (float, optional): Height above the ground. Defaults to 0.
        debug (bool, optional): If True, return intermediate calculation values.
            Defaults to False.

    Returns:
        float: The derivative of the visibility function. If phi == 0, then return
            = + or - np.Inf, depending on other inputs.
        tuple: If debug is True, the function also returns the intermediate
            calculations: phidot, a1dot, a2dot, and the components of the phidot
            calculation.
    """
    for vec in [r1, r1dot, r2, r2dot]:
        assert vec.ndim <= 2

    # convert to column vectors if not already
    r1, r1dot, r2, r2dot = [
        atleast_2d(vec).reshape(3, 1) for vec in [r1, r1dot, r2, r2dot]
    ]

    RE_prime = RE + hg

    r1_mag = norm(r1)
    r2_mag = norm(r2)

    a1dot = RE_prime * r1mag_dot / (r1_mag**2 * sin(a1))
    a2dot = RE_prime * r2mag_dot / (r2_mag**2 * sin(a2))

    # if phi == 0 (can happen when position vectors are colinear), then component0 = inf
    component0 = 1 / (r1_mag**2 * r2_mag**2 * sin(phi))
    component1 = -(r1dot.T @ r2 + r1.T @ r2dot) * r1_mag * r2_mag
    component2 = (r1mag_dot * r2_mag + r1_mag * r2mag_dot) * r1.T @ r2

    # convert to scalar
    component1 = component1.item()
    component2 = component2.item()

    # if component0 == inf, then phidot = + or - inf
    phidot = component0 * (component1 + component2)

    # if phidot == inf, then vis_der = inf, and likewise with -inf
    vis_der = a1dot + a2dot - phidot

    if debug:
        return (
            vis_der,
            phidot,
            a1dot,
            a2dot,
            component0,
            component1,
            component2,
        )
    else:
        return vis_der, phidot, a1dot, a2dot


def calcVisAndDerVis(
    r1: ndarray,
    r1dot: ndarray,
    r1mag_dot: float,
    r2: ndarray,
    r2dot: ndarray,
    r2mag_dot: float,
    RE: float,
    hg: float = 0,
) -> tuple[float, float]:
    """Calculate visibility and derivative between two points in space.

    Args:
        r1 (ndarray): Position vector of the first point.
        r1dot (ndarray): Velocity vector of the first point.
        r1mag_dot (float): Time derivative of the magnitude of the first object's
            position vector.
        r2 (ndarray): Position vector of the second point.
        r2dot (ndarray): Velocity vector of the second point.
        r2mag_dot (float): Time derivative of the magnitude of the second object's
            position vector.
        RE (float): Earth's radius.
        hg (float, optional): Height of the observer above the Earth's
        surface. Defaults to 0.

    Returns:
        float: The visibility function value (continuous).
        float: The time derivative of the visibility function.
    """
    # This is a shortcut function, so discard extra outputs
    vis, phi, a1, a2 = visibilityFunc(r1, r2, RE, hg)
    der_vis, _, _, _ = visDerivative(
        r1, r1dot, r1mag_dot, r2, r2dot, r2mag_dot, a1, a2, phi, RE, hg
    )

    return vis, der_vis
