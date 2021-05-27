from abc import ABC, abstractmethod


class Overlay(ABC):
    __res_key = None

    @property
    @abstractmethod
    def resolutions(self) -> dict:
        pass

    @property
    def res(self) -> str:
        return self.__res_key

    def get_input(self) -> None:
        selections = list(enumerate(self.resolutions.keys()))
        if(not len(selections) > 1):
            self.__res_key = selections[0][1]
            return
        else:
            print("Select Display Resolution:", "________________________\n", sep="\n")
            for idx, key in selections:
                print(f"{idx + 1}. {key}")
            print("________________________\n")
            while True:
                val = input("option: ")
                try:
                    val = int(val)
                except:
                    print("not a valid option")
                    continue
                if not (val >= 1 and val <= len(selections)):
                    print("not a valid option")
                else:
                    self.__res_key = selections[val - 1][1]
                    return
