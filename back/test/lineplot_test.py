from api.services.boardImpl import Board

import pytest # type: ignore


class TestLineplot:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.board = Board(1, 1, 'media/test.csv')
    
    def test_xy_setting_succeed1(self):
        self.board.choose('lineplot', 1, 1)
        
        # (Num, Num)
        self.board.set(
            1, 1,
            self.board.numerical_variables[0],
            self.board.numerical_variables[1]
        )
    
    def test_xy_setting_fail1(self):
        self.board.choose('lineplot', 1, 1)
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
    
    def test_xy_setting_fail2(self):
        self.board.choose("lineplot", 1, 1)
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
    
    def test_xy_setting_fail3(self):
        self.board.choose("lineplot", 1, 1)
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
    