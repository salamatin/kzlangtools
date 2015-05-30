class KazakhLemmatizer(object):

    def __init__(self):
        self.word_list = set()
        f = open('kaz.txt', 'r')
        for line in f:
            self.word_list.add(line.lower().strip())
        f.close()
        f = open('rus.txt', 'r')
        for line in f:
            self.word_list.add(line.lower().strip())
        f.close()
        print(len(self.word_list))

    NOUN_CASE_SUBSTITUTIONS = [
        ('дан', ''), ('ден', ''), ('тан', ''), ('тен', ''), ('нан', ''), ('нен', ''),           # ABL
        ('да', ''), ('де', ''), ('та', ''), ('те', ''), ('нда', ''), ('нде', ''),               # LOC
        ('дағы', ''), ('дегі', ''), ('тағы', ''), ('тегі', ''), ('ндағы', ''), ('ндегі', ''),
        ('ға', ''), ('ге', ''), ('қа', ''), ('ке', ''), ('на', ''), ('не', ''),                 # DAT
        ('а', ''), ('е', ''),
        ('дың', ''), ('дің', ''), ('тың', ''), ('тің', ''), ('ның', ''), ('нің', ''),           # GEN
        ('дікі', ''), ('тікі', ''), ('нікі', ''),
        ('ды', ''), ('ді', ''), ('ты', ''), ('ті', ''), ('ны', ''), ('ні', ''), ('н', ''),      # ACC
        ('бен', ''), ('пен', ''), ('мен', '')                                                   # INSTR

    ]

    NOUN_POSSESSIVE_SUBSTITUTIONS = [
        ('м', ''), ('ым', ''), ('ім', ''),                                                      # 1, SG
        ('бым', 'п'), ('ғым', 'қ'), ('гым', 'к'),
        ('бім', 'п'), ('гім', 'к'),

        ('мыз', ''), ('ымыз', ''), ('міз', ''), ('іміз', ''),                                   # 1, P
        ('бымыз', 'п'), ('ғымыз', 'қ'), ('гымыз', 'к'),
        ('біміз', 'п'), ('гіміз', 'к'),

        ('ң', ''), ('ың', ''), ('ің', ''),                                                      # 2, SG/P, FAM
        ('бың', 'п'), ('ғың', 'қ'), ('гың', 'к'),
        ('бің', 'п'), ('гің', 'к'),

        ('ңыз', ''), ('ыңыз', ''), ('ңіз', ''), ('іңіз', ''),                                   # 2, SG/P, FORM
        ('быңыз', 'п'), ('ғыңыз', 'қ'), ('гыңыз', 'к'),
        ('біңіз', 'п'), ('гіңіз', 'к'),

        ('ы', ''), ('сы', ''), ('і', ''), ('сі', ''),                                           # 3, SG/P
        ('бы', 'п'), ('ғы', 'қ'), ('гы', 'к'),
        ('бі', 'п'), ('гі', 'к')
    ]

    # These words drop a vowel when forming possessives
    NOUN_POSSESSIVE_EXCEPTIONS = [
        ('орн', 'орын'), ('қарн', 'қарын'), ('көрк', 'көрік'), ('ерк', 'ерік'), ('әрп', 'әріп')
    ]

    NOUN_NUMBER_SUBSTITUTIONS = [
        ('дар', ''), ('дер', ''), ('тар', ''), ('тер', ''), ('лар', ''), ('лер', '')
    ]

    NOUN_PERSONAL_SUBSTITUTIONS = [
        ('мын', ''), ('мін', ''), ('бын', ''), ('бін', ''), ('пын', ''), ('пін', ''),           # 1, SG
        ('мыз', ''), ('міз', ''), ('быз', ''), ('біз', ''), ('пыз', ''), ('піз', ''),           # 1, P
        ('сың', ''), ('сің', ''),                                                               # 2, SG, FAM
        ('сыңдар', ''), ('сіңдер', ''),                                                         # 2, P, FAM
        ('сыз', ''), ('сіз', ''),                                                               # 2, SG, FORM
        ('сыздар', ''), ('сіздер', '')                                                          # 2, P, FORM
    ]

    NOUN_SUBSTITUTION_RULES = [NOUN_CASE_SUBSTITUTIONS, NOUN_POSSESSIVE_SUBSTITUTIONS, NOUN_POSSESSIVE_EXCEPTIONS,
                               NOUN_NUMBER_SUBSTITUTIONS]

    def lemmatize(self, word, part_of_speech = 'n'):

        def apply_rule(forms, rule):
            new_forms = list(forms)
            for form in forms:
                for old, new in rule:
                    if form.endswith(old):
                        new_forms.append(form[:-len(old)] + new)
            return new_forms

        def filter_forms(forms):
            print(forms)
            result = []
            for form in forms:
                if form in self.word_list:
                    result.append(form)
            if result:
                return result
            else:
                return forms[0]

        forms = [word]

        for rule in self.NOUN_SUBSTITUTION_RULES:
            forms = apply_rule(forms, rule)
        return filter_forms(forms)