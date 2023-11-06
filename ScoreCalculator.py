import CheckWin

class ScoreCalculator:
    def __init__(self, hand, dealer=False, tsumo=False, wind=None, round_wind=None):
        self.hand = hand
        self.score = 0
        self.fu = 20
        self.han = 4
        self.yaku = []
        self.is_yakuman = False
        self.is_dealer = dealer
        self.is_tsumo = tsumo
        self.wind = wind
        self.round_wind = round_wind
        self.yaku_level = ''
        self.kyoutaku = 0
        self.honba = 0

    def identify_yaku(self):
        # Identifying yaku is a complex process and depends on hand composition.
        # This is a placeholder for the logic to identify yaku.
        pass

    def calculate_fu(self):
        # This is a placeholder for the logic to calculate fu.
        pass

    def calculate_han(self):
        # This is a placeholder for the logic to calculate han.
        pass

    def calculate_score(self):
        # Check if yakuman
        if self.han >= 13:
            self.is_yakuman = True
            self.yaku_level = "yakuman"
            base_points = 8000
        elif self.han >= 11:
            self.yaku_level = "sanbaiman"
            base_points = 6000
        elif self.han >= 8:
            self.yaku_level = "baiman"
            base_points = 4000
        elif self.han >= 6:
            self.yaku_level = "haneman"
            base_points = 3000
        elif self.han == 5:
            self.yaku_level = "mangan"
            base_points = 2000
        else:
            # If han is less than 5, calculate the base score with the formula m x 2^(2+han)
            base_points = self.fu * (2 ** (2 + self.han))
            # If the score is higher than mangan, it's rounded up to mangan
            base_points = min(base_points, 2000)

        # Calculate the total score for the winner, rounded to the nearest hundred
        if self.is_dealer:
            if self.is_tsumo:
                self.score = (base_points * 2) * 3  # Dealer tsumo, all players pay
                main_score = base_points * 2
                others_score = base_points * 2
            else:
                self.score = base_points * 6  # Dealer ron, paid by discarding player
                main_score = base_points * 6
                others_score = 0

        else:
            if self.is_tsumo:
                self.score = (base_points * 2) + (base_points * 1) * 2  # Non-dealer tsumo, dealer pays double
                main_score = base_points * 2
                others_score = base_points * 1
            else:
                self.score = base_points * 4  # Non-dealer ron, paid by discarding player
                main_score = base_points * 4
                others_score = 0

        # Add additional points from kyoutaku and honba
        self.score += (self.kyoutaku * 1000) + (self.honba * 300)

        # Round up to the nearest hundred
        main_score = ((main_score + 99) // 100) * 100
        others_score = ((others_score + 99) // 100) * 100
        self.score = main_score + others_score * 2 + (self.kyoutaku * 1000) + (self.honba * 300)

        return {
            "total": self.score,
            "yaku_level": self.yaku_level,
            # Assuming kyoutaku_score and honba_score are calculated elsewhere and added here
            "kyoutaku": self.kyoutaku * 1000,
            "honba": self.honba * 300,
            # Assuming main_score and others_score represent payments from specific players
            "main": main_score,
            "others": others_score,
        }    

    
hand = "m123456s123p123z55"
    
score_calculator = ScoreCalculator(hand,False,False,"east","east")

score_calculator.identify_yaku()

score_calculator.calculate_fu()
score_calculator.calculate_han()

score = score_calculator.calculate_score()

print(score)



