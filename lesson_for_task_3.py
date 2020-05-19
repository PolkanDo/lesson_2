school = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
          {'school_class': '4b', 'scores': [4, 5, 2, 3, 2]},
          {'school_class': '4c', 'scores': [2, 3, 5, 3, 4]},
          {'school_class': '4d', 'scores': [3, 3, 2, 3, 2]}]


def mid_scores(schl):
    school_score = 0
    i = 0
    for school_class in schl:
        school_class['mid_score'] = sum(school_class['scores'])/len(school_class['scores'])
        school_score += school_class['mid_score']
        i += 1
        print(f"Class {school_class['school_class']} has {school_class['mid_score']} middle score.")
    school_mid_score = school_score / i
    print(f"School has {school_mid_score} middle score.")


mid_scores(school)