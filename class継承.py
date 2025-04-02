class HumanClass:
    def defend(self):
        print('防御をしました！')

class WizardClass(HumanClass):
    pass
Wizard=WizardClass()
Wizard.defend()

class HumanClass:
    def __init__(self):
        print('HumanClassのinit')
        self.hp=100

class WizardClass(HumanClass):
    def __init__(self):
        super().__init__()
        self.mp=50
    def output_info(self):
        print(f'現在のＨＰは{self.hp}で、'
              f'MPは{self.mp}です。')
        
Wizard=WizardClass()
Wizard.output_info()

class WizardClass:
    def __init__(self):
        self.mp=100
        print('WizardClassのinit')
    def cast_spell(self):
        print('呪文を唱える')

class SwordFighterClass:
    def attack_with_sword(self):
        print('剣で攻撃する')

class MagicSwordFighterClass(WizardClass,
                             SwordFighterClass):
    pass
#   classの中身が空の時に一時的にpassを使う
msf=MagicSwordFighterClass()
msf.cast_spell()
msf.attack_with_sword()


