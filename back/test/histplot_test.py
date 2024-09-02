from api.services.boardImpl import Board

import pytest # type: ignore


class TestHistplot:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.board = Board(1, 1, "media/test.csv")
        self.board.choose("histplot", 1, 1)
    
    def test_xy_setting_succeed1(self):
        # (Num, None)
        self.board.set(
            1, 1,
            self.board.numerical_variables[0],
            None
        )
    
    def test_xy_setting_fail1(self):
        try:
            # (Num, Num)
            self.board.set(
                1, 1,
                self.board.numerical_variables[0],
                self.board.numerical_variables[0]
            )
        except:
            assert True
            return
        assert False
    
    def test_xy_setting_fail2(self):
        try:
            # (Num, Cat)
            self.board.set(
                1, 1,
                self.board.numerical_variables[0],
                self.board.categorical_variables[0]
            )
        except:
            assert True
            return
        assert False
    
    def test_xy_setting_fail3(self):
        try:
            # (Cat, Num)
            self.board.set(
                1, 1,
                self.board.categorical_variables[0],
                self.board.numerical_variables[0]
            )
        except:
            assert True
            return
        assert False
    
    def test_xy_setting_fail4(self):
        try:
            # (Cat, Cat)
            self.board.set(
                1, 1,
                self.board.categorical_variables[0],
                self.board.categorical_variables[0]
            )
        except:
            assert True
            return
        assert False