# project.py


import pandas as pd
import numpy as np
from pathlib import Path

import plotly.express as px


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def get_assignment_names(grades):
    assignment_names = \
    list(
        map(
            lambda x : x.split(' - ')[0], 
            list(grades.columns)
            )
        )

    assignments_dict = {
        'lab': np.unique(np.array(list(
            filter(lambda x: 'lab' in x, assignment_names)
        ))).tolist(),
        'project': np.unique(np.array(list(
                filter(lambda x: 'project' in x and 'checkpoint' not in x and 'free_response' not in x, assignment_names)
        ))).tolist(),
        'midterm': np.unique(np.array(list(
            filter(lambda x: 'Midterm' in x, assignment_names)
        ))).tolist(),
        'final': np.unique(np.array(list(
            filter(lambda x: 'Final' in x, assignment_names)
        ))).tolist(),
        'disc': np.unique(np.array(list(
            filter(lambda x: 'discussion' in x, assignment_names)
        ))).tolist(),
        'checkpoint': np.unique(np.array(list(
            filter(lambda x: 'checkpoint' in x, assignment_names)
        ))).tolist(),
    }

    return assignments_dict


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def projects_total(grades):
    names = get_assignment_names(grades)
    projects = names['project']
    project_free_responses = list(map(lambda name: name + '_free_response', projects))
    project_max_points = list(map(lambda name: name + ' - Max Points', projects))
    project_max_free_responses = list(map(lambda name: name + '_free_response - Max Points', projects))


    grades_only = grades[projects].copy()

    for i in range(len(projects)):
        try:
            num = grades[projects[i]].fillna(0) + grades[project_free_responses[i]].fillna(0)
            denom = grades[project_max_points[i]] + grades[project_max_free_responses[i]].fillna(0)
        
        except KeyError:
            num = (grades[projects[i]].fillna(0))
            denom = grades[project_max_points[i]]
            
        grades_only[projects[i]] = num / denom

    return grades_only.sum(axis=1)/len(projects)


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def lateness_penalty(col):
    def tardiness(after_due):
        """
        Assumes `after_due` is in HH:MM:SS format.
        Returns the penalty multiplier.
        """

        converted_time_list = after_due.split(':')
        converted_time = int(converted_time_list[0]) * 3600 + int(converted_time_list[1]) * 60 + int(converted_time_list[2])
        penalties = {0: 1.0, 1: 0.9, 2: 0.7, 3: 0.4}

        GRACE_PERIOD = 2 * 60 * 60
        ONE_WEEK = 7 * 24 * 60 * 60
        TWO_WEEKS = 2 * ONE_WEEK

        if converted_time <= GRACE_PERIOD:
            return penalties[0]
        if converted_time <= ONE_WEEK:
            return penalties[1]
        elif converted_time <= TWO_WEEKS:
            return penalties[2]
        return penalties[3]

    return col.fillna('00:00:00').apply(tardiness)

# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def process_labs(grades):
    names = get_assignment_names(grades)
    labs = grades[names['lab']].fillna(0)
    labs_lateness = list(map(lambda name: name + ' - Lateness (H:M:S)', labs))
    labs_max_points = list(map(lambda name: name + ' - Max Points', labs))

    penalties = grades[labs_lateness].fillna(0).apply(lateness_penalty)
    max_points = grades[labs_max_points].fillna(0)

    return (labs * penalties.values)/max_points.values


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def lab_total(processed):

    drops = processed.T.apply(min)
    drops

    lab_grades = (processed.sum(axis=1) - drops)/(len(processed.columns) - 1)

    return lab_grades

# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def total_points(grades):
    project_grade = projects_total(grades)
    lab_grade = lab_total(process_labs(grades))

    names = get_assignment_names(grades)
    checkpoints = grades[names['checkpoint']]
    checkpoints_max_points = list(map(lambda name: name + ' - Max Points', checkpoints))
    discussions = grades[names['disc']]
    discussions_max_points = list(map(lambda name: name + ' - Max Points', discussions))
    midterms = grades[names['midterm']]
    midterms_max_points = list(map(lambda name: name + ' - Max Points', midterms))
    finals = grades[names['final']]
    finals_max_points = list(map(lambda name: name + ' - Max Points', finals))

    checkpoint_grade = (checkpoints.fillna(0)/grades[checkpoints_max_points].values).mean(axis=1)
    discussion_grade = (discussions.fillna(0)/grades[discussions_max_points].values).mean(axis=1)
    midterm_grade = (midterms.fillna(0)/grades[midterms_max_points].values).mean(axis=1)
    finals_grade = (finals.fillna(0)/grades[finals_max_points].values).mean(axis=1)

    final_grade = (0.2 * lab_grade) + (0.3 * project_grade) + (0.025 * checkpoint_grade) + (0.025 * discussion_grade) + (0.15 * midterm_grade) + (0.3 * finals_grade)
    return final_grade


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def final_grades(total):
    def letter_grade(grade):
        """
        Converts a numeric final grade to a letter grade.
        """
        if grade >= 0.9:
            return 'A'
        elif grade >= 0.8:
            return 'B'
        elif grade >= 0.7:
            return 'C'
        elif grade >= 0.6:
            return 'D'
        else:
            return 'F'
        
    return total.apply(letter_grade)

def letter_proportions(total):
    letter_grades = final_grades(total)
    props = letter_grades.value_counts(normalize=True)
    return props


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def raw_redemption(final_breakdown, question_numbers):
    ...
    
def combine_grades(grades, raw_redemption_scores):
    ...


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def z_score(ser):
    ...
    
def add_post_redemption(grades_combined):
    ...


# ---------------------------------------------------------------------
# QUESTION 10
# ---------------------------------------------------------------------


def total_points_post_redemption(grades_combined):
    ...
        
def proportion_improved(grades_combined):
    ...


# ---------------------------------------------------------------------
# QUESTION 11
# ---------------------------------------------------------------------


def section_most_improved(grades_analysis):
    ...
    
def top_sections(grades_analysis, t, n):
    ...


# ---------------------------------------------------------------------
# QUESTION 12
# ---------------------------------------------------------------------


def rank_by_section(grades_analysis):
    ...







# ---------------------------------------------------------------------
# QUESTION 13
# ---------------------------------------------------------------------


def letter_grade_heat_map(grades_analysis):
    ...
