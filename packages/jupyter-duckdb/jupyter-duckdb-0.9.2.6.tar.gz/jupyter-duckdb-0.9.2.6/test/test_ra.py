import pytest

import duckdb_kernel.parser.elements.binary as BinaryOperators
import duckdb_kernel.parser.elements.unary as UnaryOperators
from duckdb_kernel.parser import RAParser
from duckdb_kernel.parser.elements import RAOperand, LogicElement
from . import Connection


def test_case_insensitivity():
    for query in (
            'users',
            'Users',
            'USERS',
            'userS'
    ):
        root = RAParser.parse_query(query)

        # root is an RAOperand
        assert isinstance(root, RAOperand)

        # Root's name is the relation name in whatever case
        # it has been written.
        assert root.name == query

        # execute to test case insensitivity
        with Connection() as con:
            assert con.execute_ra(root) == [
                (1, 'Alice'),
                (2, 'Bob'),
                (3, 'Charlie')
            ]


def test_binary_operator_cross():
    for query in (
            r'shows x seasons',
    ):
        root = RAParser.parse_query(query)

        assert isinstance(root, BinaryOperators.Cross)
        assert isinstance(root.left, RAOperand) and root.left.name == 'shows'
        assert isinstance(root.right, RAOperand) and root.right.name == 'seasons'

        with Connection() as con:
            assert con.execute_ra(root) == [
                (1, 'Show 1', 1, 1, 'Show 1 / Season 1'),
                (1, 'Show 1', 1, 2, 'Show 2 / Season 1'),
                (1, 'Show 1', 2, 1, 'Show 1 / Season 2'),
                (1, 'Show 1', 2, 2, 'Show 2 / Season 2'),
                (2, 'Show 2', 1, 1, 'Show 1 / Season 1'),
                (2, 'Show 2', 1, 2, 'Show 2 / Season 1'),
                (2, 'Show 2', 2, 1, 'Show 1 / Season 2'),
                (2, 'Show 2', 2, 2, 'Show 2 / Season 2')
            ]


def test_binary_operator_difference():
    for query in (
            r'users \ banned_users',
    ):
        root = RAParser.parse_query(query)

        assert isinstance(root, BinaryOperators.Difference)
        assert isinstance(root.left, RAOperand) and root.left.name == 'users'
        assert isinstance(root.right, RAOperand) and root.right.name == 'banned_users'

        with Connection() as con:
            assert con.execute_ra(root) == [
                (1, 'Alice'),
                (3, 'Charlie')
            ]


def test_binary_operator_division():
    for query in (
            r'π [show_id, season_number, episode_number] (episodes) ÷ π [ episode_number ] (σ [ show_id = 1 AND season_number = 1 ] (episodes))',
            r'π [show_id, season_number, episode_number] (episodes) : π [ episode_number ] (σ [ show_id = 1 AND season_number = 1 ] (episodes))',
    ):
        root = RAParser.parse_query(query)

        assert isinstance(root, BinaryOperators.Division)
        assert isinstance(root.left, UnaryOperators.Projection)
        assert isinstance(root.left.target, RAOperand) and root.left.target.name == 'episodes'
        assert isinstance(root.right, UnaryOperators.Projection)
        assert isinstance(root.right.target, UnaryOperators.Selection)
        assert isinstance(root.right.target.target, RAOperand) and root.right.target.target.name == 'episodes'

        with Connection() as con:
            assert con.execute_ra(root) == [
                (1, 1),
                (1, 2)
            ]


def test_binary_operator_intersection():
    for query in (
            r'users ∩ banned_users',
            r'users cap banned_users'
    ):
        root = RAParser.parse_query(query)

        assert isinstance(root, BinaryOperators.Intersection)
        assert isinstance(root.left, RAOperand) and root.left.name == 'users'
        assert isinstance(root.right, RAOperand) and root.right.name == 'banned_users'

        with Connection() as con:
            assert con.execute_ra(root) == [
                (2, 'Bob')
            ]


def test_binary_operator_join():
    for query in (
            r'shows ⋈ seasons',
            r'shows join seasons'
    ):
        root = RAParser.parse_query(query)

        assert isinstance(root, BinaryOperators.Join)
        assert isinstance(root.left, RAOperand) and root.left.name == 'shows'
        assert isinstance(root.right, RAOperand) and root.right.name == 'seasons'

        with Connection() as con:
            assert con.execute_ra(root) == [
                (1, 'Show 1', 1, 'Show 1 / Season 1'),
                (1, 'Show 1', 2, 'Show 1 / Season 2'),
                (2, 'Show 2', 1, 'Show 2 / Season 1'),
                (2, 'Show 2', 2, 'Show 2 / Season 2')
            ]


def test_binary_operator_union():
    for query in (
            r'users ∪ banned_users',
            r'users cup banned_users'
    ):
        root = RAParser.parse_query(query)

        assert isinstance(root, BinaryOperators.Union)
        assert isinstance(root.left, RAOperand) and root.left.name == 'users'
        assert isinstance(root.right, RAOperand) and root.right.name == 'banned_users'

        with Connection() as con:
            assert con.execute_ra(root) == [
                (1, 'Alice'),
                (2, 'Bob'),
                (3, 'Charlie'),
                (4, 'David')
            ]


def test_unary_operator_projection():
    with Connection() as con:
        for query in (
                r'π id users',
                r'π [ id ] users',
                r'π [ id ] ( users )',
                r'π[id](users)',
                r'Pi id users',
                r'Pi [ id ] users',
                r'Pi [ id ] ( users )',
                r'Pi[id](users)'
        ):
            root = RAParser.parse_query(query)

            assert isinstance(root, UnaryOperators.Projection)
            assert isinstance(root.arg, LogicElement)
            assert isinstance(root.target, RAOperand) and root.target.name == 'users'

            assert con.execute_ra(root) == [
                (1,),
                (2,),
                (3,)
            ]

        for query in (
                r'π id π id, username users',
                r'π [ id ] (π [ id, username ] (users))',
                r'π[id]π[id,username]users',
                r'Pi id Pi id, username users',
                r'Pi [ id ] (Pi [ id, username ] (users))',
                r'Pi[id]Pi[id,username]users'
        ):
            root = RAParser.parse_query(query)

            assert isinstance(root, UnaryOperators.Projection)
            assert isinstance(root.arg, LogicElement)
            assert isinstance(root.target, UnaryOperators.Projection)
            assert isinstance(root.target.arg, LogicElement)
            assert isinstance(root.target.target, RAOperand) and root.target.target.name == 'users'

            assert con.execute_ra(root) == [
                (1,),
                (2,),
                (3,)
            ]


def test_unary_operator_rename():
    for query in (
            r'β id2 ← id users',
            r'β [ id2 ← id ] users',
            r'β [ id2 ← id ] ( users )',
            r'β[id2←id](users)',
            r'Beta id2 ← id users',
            r'Beta [ id2 ← id ] users',
            r'Beta [ id2 ← id ] ( users )',
            r'Beta[id2←id](users)',
            r'Beta id2 <- id users',
            r'Beta [ id2 <- id ] users',
            r'Beta [ id2 <- id ] ( users )',
            r'Beta[id2<-id](users)'
    ):
        root = RAParser.parse_query(query)

        assert isinstance(root, UnaryOperators.Rename)
        assert isinstance(root.arg, LogicElement)
        assert isinstance(root.target, RAOperand) and root.target.name == 'users'

    for query in (
            r'β id ← id2 β id2 ← id users',
            r'β [id ← id2] (β [id2 ← id] (users))',
            r'βid←id2βid2←id users',
            r'beta id ← id2 beta id2 ← id users',
            r'beta [id ← id2] (beta [id2 ← id] (users))',
            r'beta id←id2 beta id2←id users',
            r'beta id <- id2 beta id2 <- id users',
            r'beta [id <- id2] (beta [id2 <- id] (users))',
            r'beta id<-id2 beta id2<-id users'
    ):
        root = RAParser.parse_query(query)

        assert isinstance(root, UnaryOperators.Rename)
        assert isinstance(root.arg, LogicElement)
        assert isinstance(root.target, UnaryOperators.Rename)
        assert isinstance(root.target.arg, LogicElement)
        assert isinstance(root.target.target, RAOperand) and root.target.target.name == 'users'


def test_unary_operator_selection():
    with Connection() as con:
        for query in (
                r'σ id > 1 users',
                r'σ [ id > 1 ] users',
                r'σ [ id > 1 ] ( users )',
                r'σ[id>1](users)',
                r'Sigma id > 1 users',
                r'Sigma [ id > 1 ] users',
                r'Sigma [ id > 1 ] ( users )',
                r'Sigma[id>1](users)'
        ):
            root = RAParser.parse_query(query)

            assert isinstance(root, UnaryOperators.Selection)
            assert isinstance(root.target, RAOperand) and root.target.name == 'users'
            assert isinstance(root.arg, LogicElement)

            assert con.execute_ra(root) == [
                (2, 'Bob'),
                (3, 'Charlie')
            ]

        for query in (
                r'σ id > 1 σ id > 0 users',
                r'σ [ id > 1 ] (σ [id > 1] (users))',
                r'σ[id>1]σ[id>1]users',
                r'Sigma id > 1 Sigma id > 0 users',
                r'Sigma [ id > 1 ] (Sigma [id > 1] (users))',
                r'Sigma[id>1]Sigma[id>1]users'
        ):
            root = RAParser.parse_query(query)

            assert isinstance(root, UnaryOperators.Selection)
            assert isinstance(root.arg, LogicElement)
            assert isinstance(root.target, UnaryOperators.Selection)
            assert isinstance(root.target.arg, LogicElement)
            assert isinstance(root.target.target, RAOperand) and root.target.target.name == 'users'

            assert con.execute_ra(root) == [
                (2, 'Bob'),
                (3, 'Charlie')
            ]


def test_unary_evaluation_order():
    root = RAParser.parse_query(r'π [ id2 ] β [ id2 ← id ] (users)')
    assert isinstance(root, UnaryOperators.Projection)
    assert isinstance(root.target, UnaryOperators.Rename)

    root = RAParser.parse_query(r'β [ id2 ← id ] π [ id ] (users)')
    assert isinstance(root, UnaryOperators.Rename)
    assert isinstance(root.target, UnaryOperators.Projection)

    root = RAParser.parse_query(r'π [ id ] σ [ id > 1 ] (users)')
    assert isinstance(root, UnaryOperators.Projection)
    assert isinstance(root.target, UnaryOperators.Selection)

    root = RAParser.parse_query(r'σ [ id > 1 ] π [ id ] (users)')
    assert isinstance(root, UnaryOperators.Selection)
    assert isinstance(root.target, UnaryOperators.Projection)

    root = RAParser.parse_query(r'σ [ id2 > 1 ] β [ id2 ← id ] (users)')
    assert isinstance(root, UnaryOperators.Selection)
    assert isinstance(root.target, UnaryOperators.Rename)

    root = RAParser.parse_query(r'β [ id2 ← id ] σ [ id > 1 ] (users)')
    assert isinstance(root, UnaryOperators.Rename)
    assert isinstance(root.target, UnaryOperators.Selection)


def test_binary_evaluation_order():
    # difference <-> union
    root = RAParser.parse_query(r'a \ b ∪ c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Union)

    root = RAParser.parse_query(r'a ∪ b \ c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Union)

    # difference <-> intersection
    root = RAParser.parse_query(r'a \ b ∩ c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Intersection)

    root = RAParser.parse_query(r'a ∩ b \ c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Intersection)

    # difference <-> join
    root = RAParser.parse_query(r'a \ b ⋈ c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Join)

    root = RAParser.parse_query(r'a ⋈ b \ c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Join)

    # difference <-> cross
    root = RAParser.parse_query(r'a \ b x c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Cross)

    root = RAParser.parse_query(r'a x b \ c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Cross)

    # difference <-> division
    root = RAParser.parse_query(r'a \ b ÷ c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Division)

    root = RAParser.parse_query(r'a ÷ b \ c')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Division)

    # union <-> intersection
    root = RAParser.parse_query(r'a ∪ b ∩ c')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Intersection)

    root = RAParser.parse_query(r'a ∩ b ∪ c')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Intersection)

    # union <-> join
    root = RAParser.parse_query(r'a ∪ b ⋈ c')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Join)

    root = RAParser.parse_query(r'a ⋈ b ∪ c')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Join)

    # union <-> cross
    root = RAParser.parse_query(r'a ∪ b x c')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Cross)

    root = RAParser.parse_query(r'a x b ∪ c')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Cross)

    # union <-> division
    root = RAParser.parse_query(r'a ∪ b ÷ c')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Division)

    root = RAParser.parse_query(r'a ÷ b ∪ c')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Division)

    # intersection <-> join
    root = RAParser.parse_query(r'a ∩ b ⋈ c')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Join)

    root = RAParser.parse_query(r'a ⋈ b ∩ c')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Join)

    # intersection <-> cross
    root = RAParser.parse_query(r'a ∩ b x c')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Cross)

    root = RAParser.parse_query(r'a x b ∩ c')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Cross)

    # intersection <-> division
    root = RAParser.parse_query(r'a ∩ b ÷ c')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Division)

    root = RAParser.parse_query(r'a ÷ b ∩ c')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Division)

    # join <-> cross
    root = RAParser.parse_query(r'a ⋈ b x c')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Cross)

    root = RAParser.parse_query(r'a x b ⋈ c')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Cross)

    # join <-> division
    root = RAParser.parse_query(r'a ⋈ b ÷ c')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Division)

    root = RAParser.parse_query(r'a ÷ b ⋈ c')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Division)

    # cross <-> division
    root = RAParser.parse_query(r'a x b ÷ c')
    assert isinstance(root, BinaryOperators.Cross)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, BinaryOperators.Division)

    root = RAParser.parse_query(r'a ÷ b x c')
    assert isinstance(root, BinaryOperators.Cross)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, BinaryOperators.Division)


def test_mixed_evaluation_order():
    # difference <-> projection
    root = RAParser.parse_query(r'a \ π [ id ] b')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Projection)

    root = RAParser.parse_query(r'π [ id ] a \ b')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Projection)

    # difference <-> rename
    root = RAParser.parse_query(r'a \ β [ id2 ← id ] b')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Rename)

    root = RAParser.parse_query(r'β [ id2 ← id ] a \ b')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Rename)

    # difference <-> selection
    root = RAParser.parse_query(r'a \ σ [ id > 1 ] b')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Selection)

    root = RAParser.parse_query(r'σ [ id > 1 ] a \ b')
    assert isinstance(root, BinaryOperators.Difference)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Selection)

    # union <-> projection
    root = RAParser.parse_query(r'a ∪ π [ id ] b')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Projection)

    root = RAParser.parse_query(r'π [ id ] a ∪ b')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Projection)

    # union <-> rename
    root = RAParser.parse_query(r'a ∪ β [ id2 ← id ] b')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Rename)

    root = RAParser.parse_query(r'β [ id2 ← id ] a ∪ b')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Rename)

    # union <-> selection
    root = RAParser.parse_query(r'a ∪ σ [ id > 1 ] b')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Selection)

    root = RAParser.parse_query(r'σ [ id > 1 ] a ∪ b')
    assert isinstance(root, BinaryOperators.Union)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Selection)

    # intersection <-> projection
    root = RAParser.parse_query(r'a ∩ π [ id ] b')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Projection)

    root = RAParser.parse_query(r'π [ id ] a ∩ b')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Projection)

    # intersection <-> rename
    root = RAParser.parse_query(r'a ∩ β [ id2 ← id ] b')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Rename)

    root = RAParser.parse_query(r'β [ id2 ← id ] a ∩ b')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Rename)

    # intersection <-> selection
    root = RAParser.parse_query(r'a ∩ σ [ id > 1 ] b')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Selection)

    root = RAParser.parse_query(r'σ [ id > 1 ] a ∩ b')
    assert isinstance(root, BinaryOperators.Intersection)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Selection)

    # join <-> projection
    root = RAParser.parse_query(r'a ⋈ π [ id ] b')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Projection)

    root = RAParser.parse_query(r'π [ id ] a ⋈ b')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Projection)

    # join <-> rename
    root = RAParser.parse_query(r'a ⋈ β [ id2 ← id ] b')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Rename)

    root = RAParser.parse_query(r'β [ id2 ← id ] a ⋈ b')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Rename)

    # join <-> selection
    root = RAParser.parse_query(r'a ⋈ σ [ id > 1 ] b')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Selection)

    root = RAParser.parse_query(r'σ [ id > 1 ] a ⋈ b')
    assert isinstance(root, BinaryOperators.Join)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Selection)

    # cross <-> projection
    root = RAParser.parse_query(r'a x π [ id ] b')
    assert isinstance(root, BinaryOperators.Cross)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Projection)

    root = RAParser.parse_query(r'π [ id ] a x b')
    assert isinstance(root, BinaryOperators.Cross)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Projection)

    # cross <-> rename
    root = RAParser.parse_query(r'a x β [ id2 ← id ] b')
    assert isinstance(root, BinaryOperators.Cross)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Rename)

    root = RAParser.parse_query(r'β [ id2 ← id ] a x b')
    assert isinstance(root, BinaryOperators.Cross)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Rename)

    # cross <-> selection
    root = RAParser.parse_query(r'a x σ [ id > 1 ] b')
    assert isinstance(root, BinaryOperators.Cross)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Selection)

    root = RAParser.parse_query(r'σ [ id > 1 ] a x b')
    assert isinstance(root, BinaryOperators.Cross)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Selection)

    # division <-> projection
    root = RAParser.parse_query(r'a ÷ π [ id ] b')
    assert isinstance(root, BinaryOperators.Division)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Projection)

    root = RAParser.parse_query(r'π [ id ] a ÷ b')
    assert isinstance(root, BinaryOperators.Division)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Projection)

    # division <-> rename
    root = RAParser.parse_query(r'a ÷ β [ id2 ← id ] b')
    assert isinstance(root, BinaryOperators.Division)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Rename)

    root = RAParser.parse_query(r'β [ id2 ← id ] a ÷ b')
    assert isinstance(root, BinaryOperators.Division)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Rename)

    # division <-> selection
    root = RAParser.parse_query(r'a ÷ σ [ id > 1 ] b')
    assert isinstance(root, BinaryOperators.Division)
    assert isinstance(root.left, RAOperand) and isinstance(root.right, UnaryOperators.Selection)

    root = RAParser.parse_query(r'σ [ id > 1 ] a ÷ b')
    assert isinstance(root, BinaryOperators.Division)
    assert isinstance(root.right, RAOperand) and isinstance(root.left, UnaryOperators.Selection)


def test_special_queries():
    with Connection() as con:
        # Consecutive operators triggered a recursion error in a previous
        # version, leading to an infinite loop / stack overflow.
        with pytest.raises(AssertionError, match='right operand missing after x'):
            RAParser.parse_query(r'''
                users x x banned_users
            ''')

        # Enclosing parentheses are removed. In the following case
        # the parentheses may only be removed from each subquery
        # independently *after* the cross join is applied. Otherwise,
        # the result is a parsing error.
        root = RAParser.parse_query(r'''
            (
              Sigma [ id > 1 ] Pi [ username, id ] (users)
            ) x (
              Beta [ username2 <- username ] Beta [ id2 <- id ] (banned_users)
            )
        ''')

        assert isinstance(root, BinaryOperators.Cross)
        assert isinstance(root.left, UnaryOperators.Selection)
        assert isinstance(root.left.target, UnaryOperators.Projection)
        assert isinstance(root.left.target.target, RAOperand) and root.left.target.target.name == 'users'
        assert isinstance(root.right, UnaryOperators.Rename)
        assert isinstance(root.right.target, UnaryOperators.Rename)
        assert isinstance(root.right.target.target, RAOperand) and root.right.target.target.name == 'banned_users'

        assert con.execute_ra(root) == [
            ('Bob', 2, 2, 'Bob'),
            ('Bob', 2, 4, 'David'),
            ('Charlie', 3, 2, 'Bob'),
            ('Charlie', 3, 4, 'David')
        ]
