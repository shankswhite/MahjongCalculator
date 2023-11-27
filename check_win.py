import input_handler
class check_win:
    @staticmethod
    def calc_(list_):
        if len(list_)==3:
            if list_.count(list_[0]) == 3:
                return True
            elif list_[0] + list_[2] == list_[1] * 2:
                return True
            else:
                return False
        elif len(list_) == 2:
            if list_.count(list_[0]) == 2:
                return True
            else:
                return False
        else:
            if list_.count(list_[0]) == 3:
                if check_win.calc_(list_[3:]):
                    return True
            if len(list_)%3 == 2 and list_.count(list_[0]) == 2:
                if check_win.calc_(list_[2:]):
                    return True
            if list_.count(list_[0] + 1) >= 1 and list_.count(list_[0] + 2) >= 1:
                list_.pop(list_.index(list_[0] + 2))
                list_.pop(list_.index(list_[0] + 1))
                list_.pop(0)
                if check_win.calc_(list_):
                    return True
            return False

    @staticmethod
    def all_pai():
        for i in range(1,10):
            yield i
        for i in range(11,20):
            yield i
        for i in range(21,30):
            yield i
        yield 31
        yield 33
        yield 35
        yield 37
        yield 39
        yield 41
        yield 43

    #返回当前牌型胡什么
    @staticmethod
    def all_hu(list):
        ret = []
        for i in all_pai():
            hu_ = list[:]
            hu_.append(i)
            hu_.sort()
            if self.calc_(hu_):
                ret.append(i)
        return ret




tiles = input_handler.InputHandler.input_handler('123m123345p123s11z')

print(check_win.calc_(tiles))