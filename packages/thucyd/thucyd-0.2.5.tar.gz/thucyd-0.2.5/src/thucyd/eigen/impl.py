"""
-------------------------------------------------------------------------------

Implementation of the theory of consistently oriented eigenvectors.

This is a reference implementation against which performant implementations
can be compared.

-------------------------------------------------------------------------------
"""


import numpy as np
import warnings

# define API exposure
__all__ = [
    "orient_eigenvectors",
    "generate_oriented_eigenvectors",
]


"""
-------------------------------------------------------------------------------
Orientation code
-------------------------------------------------------------------------------
"""


# noinspection SpellCheckingInspection,PyPep8Naming
def orient_eigenvectors(
    V: np.ndarray,
    E: np.ndarray,
    method: str = "arcsin",
    orient_to_first_orthant: bool = False,
) -> tuple:
    """Finds `R` and `S` that orients `V S` to  within a rotation of `I`.

    The orientation is performed using rotations and reflections.

    The `arctan2` method returns angles that span [-pi, pi]. In contrast, the
    'arcsin' method returns angles that span [-pi/2, pi/2]. The preferred method
    is 'arctanz2' and 'arcsin' may be deprecated in the future.

    Parameters
    ----------
    V: np.ndarray
        Eigenvector matrix with columns vectors
    E: np.ndarray
        Eigenvalue vector whose entries are associated to the columns of V
    method: bool (default: False)
        Flag to indicate whether the first eigenvector should point within the
        first orthant of the space.
    orient_to_first_orthant: bool (default: False)
        Flag to indicate whether the first eigenvector should point within the
        first orthant of the space. Only applicable for the `arctan2` method.

    Returns
    -------
    Vor: np.ndarray
        Eigenvector matrix cast into an oriented basis, see Note 1.

    Eor: np.ndarray
        Eigenvalue vector whose entries are associated to the columns of Vor,
        see Note 2.

    sign_flip_vector: np.ndarray
        Vector of signs that was applied to (sorted) `V` such that `Vor` is
        oriented.

    theta_matrix: np.ndarray
        upper-triangular matrix of angles embedded in `Vor` with respect to the
        constituent basis in which (sorted) `V` is materialized.

    sort_indices: np.ndarray
        Permutation vector such that Vsort = V[:, sort_indices].

    Notes
    -----
    1. The columns of `Vor` are ordered such that their associated eigenvalues
       are sorted in descending order of absolute value. That the absolute
       value is taken on the eigenvalues is to treat the general case of an
       input Hermitian matrix. For data analysis, SVD yields a positive
       (semi)definite eigensystem, so negative eigenvalues are not attained.

    2. The entries of `Eor` are ordered in descending absolute value
       of the input eigenvalue vector `E`.
    """

    # handle E to ensure that it is a vector
    Evec, is_vector = handle_eigenvalue_input(E)
    if not is_vector:
        warnings.warn(
            (
                "E must be passed as a vector in future releases. "
                "Passing a matrix E will be deprecated."
            ),
            category=FutureWarning,
        )

    if method == "arcsin":
        return orient_eigenvectors_via_arcsin_method(V, Evec)
    elif method == "arctan2":
        return orient_eigenvectors_via_modified_arctan2_method(
            V, Evec, orient_to_first_orthant=orient_to_first_orthant
        )
    else:
        raise RuntimeError(
            f"Unknown method {method} -- must be 'arctan2' or 'arcsin'"
        )


# noinspection SpellCheckingInspection,PyPep8Naming
def orient_eigenvectors_via_modified_arctan2_method(
    V: np.ndarray, E: np.ndarray, orient_to_first_orthant: bool = False
) -> tuple:
    """Implements the modified `arctan2` method wherein angles in [-pi, pi].

    Parameters
    ----------
    V: np.ndarray
        Eigenvector matrix with columns vectors
    E: np.ndarray
        Eigenvalue vector whose entries are associated to the columns of V
    orient_to_first_orthant: bool (default: False)
        Flag to indicate whether the first eigenvector should point within the
        first orthant of the space.

    Returns
    -------
    Vor: np.ndarray
        Eigenvector matrix cast into an oriented basis.

    Eor: np.ndarray
        Eigenvalue vector whose entries are associated to the columns of Vor.

    sign_flip_vector: np.ndarray
        Vector of signs that was applied to (sorted) `V` such that `Vor` is
        oriented.

    theta_matrix: np.ndarray
        upper-trianglar matrix of angles embedded in `Vor` with respect to the
        constituent basis in which (sorted) `V` is matrialized.

    sort_indices: np.ndarray
        Permutation vector such that Vsort = V[:, sort_indices].
    """

    # To begin, sort (V, E) by descending absolute-value of eigenvalues in E.
    Vsort, Esort, sort_indices = sort_eigenvectors(V, E)

    # make a copy for local work
    Vwork = Vsort.copy()

    # pick off full dimension
    full_dim = Vwork.shape[0]

    # initialize storage matrix for angles
    angles_matrix = np.zeros(Vwork.shape, dtype=float)

    # initialize sign-flip vector
    sign_flip_vector = np.ones(full_dim, dtype=int)

    # create scan array of cursors as they range [0: full-dim)
    cursors = np.arange(full_dim)

    # orient the first mode into the first orthant, if requested
    cursor = 0
    if orient_to_first_orthant:
        sign_flip_vector[cursor] = 1 if Vwork[cursor, cursor] >= 0.0 else -1
        Vwork[:, cursor] *= sign_flip_vector[cursor]

    # iterate over all reducible dimensions
    for cursor in cursors[:-1]:
        # reduce the subspace dimension by 1 using a rotation matrix
        Vwork, angles_col = reduce_dimension_by_one(full_dim, cursor, Vwork)

        # persist the angles in an upper triangular matrix
        angles_matrix[cursor, :] = angles_col.T

    # for the last, irreducible dimension, flip the sign if necessary
    if Vwork[-1, -1] < 0.0:
        sign_flip_vector[-1] = -1

    # calculate Vor, the right-handed basis for Vsort
    Vor = Vsort.dot(np.diag(sign_flip_vector))

    # return work performed by this function
    return Vor, Esort, sign_flip_vector, angles_matrix, sort_indices


# noinspection SpellCheckingInspection,PyPep8Naming
def orient_eigenvectors_via_arcsin_method(
    V: np.ndarray, E: np.ndarray
) -> tuple:
    """Implements the `arcsin` method wherein angles in [-pi/2, pi/2].

    Parameters
    ----------
    V: np.ndarray
        Eigenvector matrix with columns vectors
    E: np.ndarray
        Eigenvalue vector conformant to V

    Returns
    -------
    Vor: np.ndarray
        Eigenvector matrix cast into an oriented basis.

    Eor: np.ndarray
        Eigenvalue vector conformant to Vor.

    sign_flip_vector: np.ndarray
        Vector of signs that was applied to (sorted) `V` such that `Vor` is
        oriented.

    theta_matrix: np.ndarray
        upper-trianglar matrix of angles embedded in `Vor` with respect to the
        constituent basis in which (sorted) `V` is matrialized.

    sort_indices: np.ndarray
        Permutation vector such that Vsort = V[:, sort_indices].
    """

    # To begin, sort (V, E) by descending absolute-value of eigenvalues in E.
    Vsort, Esort, sort_indices = sort_eigenvectors(V, E)

    # make a copy for local work
    Vwork = Vsort.copy()

    # pick off full dimension
    full_dim = Vwork.shape[0]

    # initialize storage matrix for angles
    angles_matrix = np.zeros(Vwork.shape)

    # initialize sign-flip vectory
    sign_flip_vector = np.zeros(full_dim)

    # create scan array of cursors as they range [0: full-dim)
    cursors = np.arange(full_dim)

    # iterate from the full dimension down to R^1
    for cursor in cursors:
        # eval sign flip
        sign_flip_vector[cursor] = 1.0 if Vwork[cursor, cursor] >= 0.0 else -1.0

        # apply the flip to the cursor column in Vsort
        Vwork[:, cursor] *= sign_flip_vector[cursor]

        # reduce the subspace dimension by one using a rotation matrix
        Vwork, angles_col = reduce_dimension_by_one(full_dim, cursor, Vwork)

        # persist the angles in an upper triangular matrix
        angles_matrix[cursor, :] = angles_col.T

    # calculate Vor, the right-handed basis for Vsort
    Vor = Vsort.dot(np.diag(sign_flip_vector))

    # return work performed by this function
    return Vor, Esort, sign_flip_vector, angles_matrix, sort_indices


# noinspection SpellCheckingInspection,PyPep8Naming
def reduce_dimension_by_one(
    full_dim: int, cursor: int, Vwork: np.ndarray
) -> tuple:
    """
    Reduces the nonaligned dimension of `Vwork` by one by rotating the subspace
    onto a constituent axis. Concretely, `Vwork` is transformed so that a 1
    appears on the diagonal pivot pointed to by `cursor`.

    As an exception, when the space is irreducible through rotation, which
    is when `cursor` points to the lowest left diagonal element, no operation
    is performed on `Vwork` by this function.

    Parameters
    ----------
    full_dim: int
        The dimension of the full space, quoted in base(1) style.
    cursor: int
        Pointer to the lower right subspace embedded in R^full_dim, quoted in
        base(0) style.
    Vwork: np.ndarray
        Current workspace matrix such that the upper-left pivots outside
        the current subspace are 1 while the lower-right subspace itself remains
        (almost surely) unaligned to the constituent basis.

    Returns
    -------
    Vwork: np.ndarray
        Updated Vwork matrix.
    angles_col: np.ndarray
        Givens rotation angles applied to input Vwork.

    Notes
    -----
    The goal is to apply rotation matrix R.T such that the current subspace
    dimension of Vwork is reduced by one. In block form,

            -            -     -            -
            | 1          |     | 1          |
     R.T x  |    *  *  * |  =  |    1       |
            |    *  *  * |     |       *  * |
            |    *  *  * |     |       *  * |
            -            -     -            -

    When `Vwork` is irreducible via rotation, matrix looks like

        -                  -
        | 1                |
        |    1             |
        |       ...        |
        |           +/- 1  |
        -                  -

    The sign of the lower right diagonal element equals det(V) where
    `V` is the original matrix of eigenvectors. Reorientation of this
    last signed value requires a reflection, but this concern is handled
    elsewhere.
    """

    # irreducible subspace
    if cursor == full_dim - 1:
        angles_col = np.zeros(full_dim)
        return Vwork, angles_col

    # reducible subspace
    # solve for rotation angles
    angles_col = solve_rotation_angles_in_subdimension_via_arctan2(
        full_dim, cursor, Vwork[:, cursor]
    )

    # construct subspace rotation matrix via a cascade of Givens rotations
    R = construct_subspace_rotation_matrix(full_dim, cursor, angles_col)

    # Apply R.T to reduce the non-identity subspace by one dimension.
    Vwork = R.T.dot(Vwork)

    # return
    return Vwork, angles_col


# noinspection SpellCheckingInspection,PyPep8Naming
def solve_rotation_angles_in_subdimension_via_arctan2(
    full_dim: int, cursor: int, Vcol: np.ndarray
) -> np.ndarray:
    """
    Solves for angles embedded in the column `Vcol` when the subspace is
    reducible through rotation. To do so, a sequence of Givens rotations is
    calculated to rotate a unit vector that points along a constituent axis
    (selected by `cursor`) into the input `Vcol` vector.

    When the subspace is irreducible then a vector of zeros is returned.

    This function implements the modified arctan2 method.

    Parameters
    ----------
    full_dim: int
        The dimension of the full space, quoted in base(1) style.
    cursor: int
        Pointer to the lower right subspace embedded in R^full_dim, quoted in
        base(0) style.
    Vcol: np.ndarray
        Column in `full_dim` whose elements at and above `cursor` will be
        matched by the rotation sequence.

    Returns
    -------
    np.ndarray
        Returns `angles_col` sized to the full dimension.

    Notes
    -----
    The recursion in this function solves for angles theta_2, theta_3, ...
    such that

        -          -     -    -
        | c2 c3 c4 |     | v1 |  <-- sub-cursor-tail
        | s2 c3 c4 |  =  | v2 |  <-- sub-cursor-head
        |   s3 c4  |     | v3 |
        |    s4    |     | v4 |
        -          -     -    -

    where {s|c}k = {sin|cos}(theta_k).

    In relation to the vector above, the modified arctan2 method is

        theta2 = arctan2(v2, v1)                  major angle
        theta3 = arctan2(v3 |sin(theta2)|, |v2|)  minor angle
        theta4 = arctan2(v4 |sin(theta3)|, |v3|)  ""

    In the presence of sparsity, where the `Vcol` contains one or more zeros,
    the tail sub-cursor have to be advanced carefully so that it always points
    to a nonzero element. The fast-path code skips this concern when `Vcol`
    is dense, and the slow-path code deals with the indexing otherwise.
    """

    # irreducible subspace
    if cursor == full_dim - 1:
        return np.zeros(full_dim)

    # create scan array of sub-cursors as they range [cursor + 1: full-dim)
    sub_cursors = np.arange(cursor, full_dim)

    # prepare for the recursion
    angles_work = np.zeros(full_dim)

    # first angle may sweep a major arc
    sub_cursor_tail = sub_cursors[0]
    sub_cursor_head = sub_cursors[1]
    angles_work[sub_cursor_head] = np.arctan2(
        Vcol[sub_cursor_head], Vcol[sub_cursor_tail]
    )

    # split code path based on whether `Vcol` contains ~zero-value elements
    eps_value = np.finfo(np.float64).eps
    if np.all(np.abs(Vcol[1:]) > eps_value):  # fast path
        # remaining angles sweep minor arcs
        for sub_cursor_head in sub_cursors[2:]:
            sub_cursor_tail = sub_cursor_head - 1
            angles_work[sub_cursor_head] = np.arctan2(
                Vcol[sub_cursor_head]
                * np.abs(np.sin(angles_work[sub_cursor_tail])),
                np.abs(Vcol[sub_cursor_tail]),
            )

    else:  # slow path
        # remaining angles sweep minor arcs
        for sub_cursor_head in sub_cursors[2:]:
            # advance the tail cursor if possible
            if np.abs(Vcol[sub_cursor_head - 1]) > eps_value:
                sub_cursor_tail = sub_cursor_head - 1

            # compute theta value
            if np.abs(Vcol[sub_cursor_head]) > eps_value:  # general case
                if sub_cursor_tail > 0:  # general case
                    arctan2_val = np.arctan2(
                        Vcol[sub_cursor_head]
                        * np.abs(np.sin(angles_work[sub_cursor_tail])),
                        np.abs(Vcol[sub_cursor_tail]),
                    )
                else:  # special case to account for all cosines in first row
                    arctan2_val = np.arctan2(
                        Vcol[sub_cursor_head],
                        np.abs(Vcol[sub_cursor_tail]),
                    )

            else:  # when head points to a zero, theta == 0
                arctan2_val = 0.0

            # record
            angles_work[sub_cursor_head] = arctan2_val

    # return work angles
    return angles_work


# noinspection SpellCheckingInspection,PyPep8Naming
def solve_rotation_angles_in_subdimension_via_arcsin(
    full_dim: int, cursor: int, Vcol: np.ndarray
) -> np.ndarray:
    """
    Solves for embedded angles necessary to rotate a unit vector pointing
    along the `cursor` axis, within `full_dim`, into the input `Vcol` vector.

    Recursive solution strategy to calculate rotation angles required to
    rotate the principal axis of a sub dimension onto an axis of its
    corresponding constituent basis.

    Parameters
    ----------
    full_dim: int
        The dimension of the full space, quoted in base(1) style.
    cursor: int
        Pointer to the lower right subspace embedded in R^full_dim, quoted in
        base(0) style.
    Vcol: np.ndarray
        Column in `full_dim` whose elements at and above `cursor` will be
        matched by the rotation sequence.

    Returns
    -------
    np.ndarray
        Returns `angles_col` sized to the full dimension.

    Notes
    -----
    The recursion in this function solves for angles theta_2, theta_3, ...
    such that

        -          -     -    -
        | c2 c3 c4 |     | v1 |
        | s2 c3 c4 |  =  | v2 |,  {s|c}k = {sin|cos}(theta_k)
        |   s3 c4  |     | v3 |
        |    s4    |     | v4 |
        -          -     -    -

    In particular, the arcsin recursion equations are implemented because
    they have better edge-case properties than the arctan recursion.
    """

    # create scan array of sub-cursors as they range [cursor + 1: full-dim)
    sub_cursors = np.arange(cursor + 1, full_dim)

    # prepare for the recursion
    angles_work = np.zeros(full_dim + 1)
    r = 1.0

    # iterate over rows in subspace to calculate full 2-pi angles
    for sub_cursor in sub_cursors[::-1]:
        y = Vcol[sub_cursor]
        r *= np.cos(angles_work[sub_cursor + 1])

        angles_work[sub_cursor] = np.arcsin(y / r) if r != 0.0 else 0.0

    # return work angles sized to full_dim
    return angles_work[:full_dim]


# noinspection SpellCheckingInspection,PyPep8Naming
def construct_subspace_rotation_matrix(
    full_dim: int, cursor: int, angles_col: np.ndarray
) -> np.ndarray:
    """
    Constructs a rotation matrix that spans the subspace indicated by the
    `cursor` by cascading a sequence of Givens rotations.

    Parameters
    ----------
    full_dim: int
        The dimension of the full space, quoted in base(1) style.
    cursor: int
        Pointer to the lower right subspace embedded in R^full_dim, quoted in
        base(0) style.
    angles_col: np.ndarray
        Rotation angles in current subspace. This is a view on `angles_matrix`
        from the outer scope.

    Returns
    -------
    np.ndarray
        Rotation matrix `R` being a cascade of Givens rotations.

    Notes
    -----
    This function constructs a cascade of Givens rotations in the following way:

    `full_dim` = 4, `cursor` = 1

    -            --            -     -            -
    | 1          || 1          |     | 1          |
    |   c  -s    ||   c     -s |  =  |    *  *  * |
    |   s   c    ||      1     |     |    *  *  * |
    |          1 ||   s      c |     |    *  *  * |
    -            --            -     -            -
          ^              ^
      theta_2,3     theta_2,4               R

    """

    # initialize R
    R = np.eye(full_dim)

    # create scan array of sub-cursors as they range [cursor + 1: full-dim)
    sub_cursors = np.arange(cursor + 1, full_dim)

    # iterate over angles (reverse order), build a Givens matrix, and apply
    for sub_cursor in sub_cursors[::-1]:
        # noinspection PyUnresolvedReferences
        R = make_givens_rotation_matrix_in_subspace(
            full_dim, cursor, sub_cursor, angles_col[sub_cursor]
        ).dot(R)

    # return the rotation matrix
    return R


# noinspection SpellCheckingInspection,PyPep8Naming
def make_givens_rotation_matrix_in_subspace(
    full_dim: int, cursor: int, sub_cursor: int, theta: float
) -> np.ndarray:
    """
    Makes a Givens rotation matrix.

    Parameters
    ----------
    full_dim: int
        The dimension of the full space, quoted in base(1) style.
    cursor: int
        Pointer to the lower right subspace embedded in R^full_dim, quoted in
        base(0) style.
    sub_cursor: int
        Pointer to the pivot position of the lower cos(.) entry.
    theta: float
        Rotation angle.

    Returns
    -------
    np.ndarray

    Notes
    -----
    A Givens matrix, such as

            -          -
            | 1        |
        R = |   c   -s |
            |     1    |
            |   s    c |
            -          -
                ^    ^
                |    |
             cursor  |
                sub-cursor

    where, in this example, full_dim = 4.

    It is up to the caller to validate the `cursor` and `sub_cursor` indexing
    into R.
    """

    # eval trig
    c = np.cos(theta)
    s = np.sin(theta)

    # construct Givens rotation matrix
    R = np.eye(full_dim)

    R[cursor, cursor] = c
    R[cursor, sub_cursor] = -s
    R[sub_cursor, cursor] = s
    R[sub_cursor, sub_cursor] = c

    # return
    return R


# noinspection SpellCheckingInspection,PyPep8Naming
def sort_eigenvectors(
    V: np.ndarray, E: np.ndarray, atol: float = 1e-6
) -> tuple:
    """
    Sorts the columns of `V` such that their corresponding eigenvalues appear
    in decreasing order of absolute values. In the special case that all
    eigenvalues are equal, no sort is performed.

    Parameters
    ----------
    V: ndarray
        Original n x n eigenvector matrix.
    E: ndarray
        Original n eigenvalue vector.
    atol: float
        Absolute tolerance when comparing eigenvalues

    Returns
    -------
    sort_indices: ndarray
        result of argsort on abs(diag(E)), (n x 1).
    Vsort: ndarray
        V[:, sort_indices] (n x n)
    Esort: ndarray
        E[sort_indices] (n)

    """

    # special case when all eigenvalues are equal
    if np.all(np.isclose(E, E[0] * np.ones_like(E), atol=atol)):
        sort_indices = np.arange(E.shape[0])
        return V, E, sort_indices

    # otherwise, argsort the absolute values of e_vector in descending order
    sort_indices = np.argsort(np.fabs(E))[::-1]

    # sort V and E based on sort_indices
    Vsort = V[:, sort_indices]
    Esort = E[sort_indices]

    # return
    return Vsort, Esort, sort_indices


# noinspection PyPep8Naming
def handle_eigenvalue_input(E: np.ndarray) -> tuple[np.ndarray, bool]:
    """Returns an eigenvalue vector regardless whether `E` is a vector or mtx.

    Parameters
    ----------
    E: ndarray
        Eigenvector object to handle, either 1D or 2D

    Returns
    -------
    ndarray
        Eigenvector object converted to a vector
    """

    # compress a matrix to a vector, else return a vector
    return (E, True) if E.ndim == 1 else (np.diag(E), False)


"""
-------------------------------------------------------------------------------
Rotation generator code
-------------------------------------------------------------------------------
"""


# noinspection SpellCheckingInspection,PyPep8Naming
def generate_oriented_eigenvectors(
    angles_matrix: np.ndarray, kth_eigenvector=None
) -> np.ndarray:
    """
    The call `orient_eigenvectors` consumes an eigenvector matrix `V` that is
    not necessarily oriented and returns `Vor`, its oriented counterpart.
    The `orient_eigenvectors` call also returns `angles_matrix`.

    This function consumes `angles_matrix` (instead of `V`) to produce `Vor`,
    the oriented eigenvector matrix.

    Recall that

    (1)    Vor = V S = R

    where `S` is a diagonal matrix with +/- 1 entries, and `R` is a rotation
    matrix. `orient_eigenvectors` computes `V S` while this function computes
    `R`.

    For a constituent basis I(n), the identity matrix, `R` rotates `I` into
    `Vor`,

    (2)    Vor = R I.

    In this way we identify `R` with the rotation that brings `I` into align-
    ment with `Vor`.

    Rotation matrix `R` itself is a cascade of rotations, one for each eigen-
    vector,

    (3)    R = R_1 R_2 ... R_n .

    Moreover, rotation R_k is itself a cascade of elemental Givens rotations.
    In R^4, the R_1 rotation is

    (4)    R_1(theta_(1,2), theta_(1,3), theta_(1,4)) =
                R_(1,2)(theta_(1,2))
                    x R_(1,3)(theta_(1,3))
                        x R_(1,4)(theta_(1,4)).

    The angles are read from `angles_matrix` such that

              -                  -
              | 0  t12  t13  t14 |  <-- row for R_1
    ang_mtx = |    0    t23  t24 |  <-- row for R_2
              |    *    0    t34 |   ...
              |    *    *    0   |
              -                  -

    Parameters
    ----------
    angles_matrix: ndarray
        Upper-triangular (n x n) matrix of angles.
    kth_eigenvector: int
        Default value is None, otherwise a base(1) indicator of the eigenvector
        to rotate into its constituent axis.

    Returns
    -------
    np.ndarray
        Resultant rotation matrix.

    Notes
    -----
    The full dimension of the space is inferred from the dimension of
    `angles_matrix`. Given a `full_dim`, the rotation matrix that corresponds
    to the kth eigenvector is constructed from elementary Givens rotations.
    In R^4, the rotation matrix for the 1st eigenvector is

    (1) R_1(theta_(1,2), theta_(1,3), theta_(1,4)) =
            R_(1,2)(theta_(1,2)) x R_(1,3)(theta_(1,3)) x R_(1,4)(theta_(1,4)).

    The rotation matrix for the full eigenbasis in R^4 is

    (2) R = R_1 R_2 R_3 R_4.

    """

    # initialize
    full_dim = angles_matrix.shape[0]

    # evaluate (3) from the notes above
    if kth_eigenvector is not None:
        # conform to function interface
        cursor = kth_eigenvector - 1
        angles_col = angles_matrix[cursor, :].T

        R = construct_subspace_rotation_matrix(full_dim, cursor, angles_col)

    # evaluate (4) from the notes above
    else:
        # initialize
        R = np.eye(full_dim)

        # create scan array across all dimensions
        cursors = np.arange(full_dim)

        # iterate over cursors
        for cursor in cursors:
            # conform to function interface
            angles_col = angles_matrix[cursor, :].T

            # build R_k.dot(R_(k+1))
            R = R.dot(
                construct_subspace_rotation_matrix(full_dim, cursor, angles_col)
            )

    # return
    return R
