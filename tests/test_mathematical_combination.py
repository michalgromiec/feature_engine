import pandas as pd
import pytest

from feature_engine.mathematical_combination import MathematicalCombinator


def test_MathematicalCombinator_all(dataframe_vartypes):
    transformer = MathematicalCombinator()

    X = transformer.fit_transform(dataframe_vartypes)

    ref = pd.DataFrame.from_dict(
        {
            'Name': ['tom', 'nick', 'krish', 'jack'],
            'City': ['London', 'Manchester', 'Liverpool', 'Bristol'],
            'Age': [20, 21, 19, 18],
            'Marks': [0.9, 0.8, 0.7, 0.6],
            'dob': pd.date_range('2020-02-24', periods=4, freq='T'),
            'sum(Age-Marks)': [20.9, 21.8, 19.7, 18.6],
            'prod(Age-Marks)': [18.0, 16.8, 13.299999999999999, 10.799999999999999],
            'mean(Age-Marks)': [10.45, 10.9, 9.85, 9.3],
            'std(Age-Marks)': [13.505739520663058, 14.28355697996826, 12.94005409571382, 12.303657992645928],
            'max(Age-Marks)': [20.0, 21.0, 19.0, 18.0],
            'min(Age-Marks)': [0.9, 0.8, 0.7, 0.6]
        }
    )

    # init params
    assert transformer.variables == ['Age', 'Marks']
    assert transformer.operations == ['sum', 'prod', 'mean', 'std', 'max', 'min']
    # fit params
    assert transformer.input_shape_ == (4, 5)
    assert transformer.combination_dict_ == {
        'sum(Age-Marks)': 'sum',
        'prod(Age-Marks)': 'prod',
        'mean(Age-Marks)': 'mean',
        'std(Age-Marks)': 'std',
        'max(Age-Marks)': 'max',
        'min(Age-Marks)': 'min'
    }
    # transform params
    pd.testing.assert_frame_equal(X, ref)


def test_MathematicalCombinator_SelectedVariables(dataframe_vartypes):
    transformer = MathematicalCombinator(variables=['Age', 'Marks'])

    X = transformer.fit_transform(dataframe_vartypes)

    ref = pd.DataFrame.from_dict(
        {
            'Name': ['tom', 'nick', 'krish', 'jack'],
            'City': ['London', 'Manchester', 'Liverpool', 'Bristol'],
            'Age': [20, 21, 19, 18],
            'Marks': [0.9, 0.8, 0.7, 0.6],
            'dob': pd.date_range('2020-02-24', periods=4, freq='T'),
            'sum(Age-Marks)': [20.9, 21.8, 19.7, 18.6],
            'prod(Age-Marks)': [18.0, 16.8, 13.299999999999999, 10.799999999999999],
            'mean(Age-Marks)': [10.45, 10.9, 9.85, 9.3],
            'std(Age-Marks)': [13.505739520663058, 14.28355697996826, 12.94005409571382, 12.303657992645928],
            'max(Age-Marks)': [20.0, 21.0, 19.0, 18.0],
            'min(Age-Marks)': [0.9, 0.8, 0.7, 0.6]
        }
    )

    # init params
    assert transformer.variables == ['Age', 'Marks']
    assert transformer.operations == ['sum', 'prod', 'mean', 'std', 'max', 'min']
    # fit params
    assert transformer.input_shape_ == (4, 5)
    assert transformer.combination_dict_ == {
        'sum(Age-Marks)': 'sum',
        'prod(Age-Marks)': 'prod',
        'mean(Age-Marks)': 'mean',
        'std(Age-Marks)': 'std',
        'max(Age-Marks)': 'max',
        'min(Age-Marks)': 'min'
    }
    # transform params
    pd.testing.assert_frame_equal(X, ref)


def test_MathematicalCombinator_SelectedVariables(dataframe_vartypes):
    transformer = MathematicalCombinator(variables=['Age', 'Marks'])

    X = transformer.fit_transform(dataframe_vartypes)

    ref = pd.DataFrame.from_dict(
        {
            'Name': ['tom', 'nick', 'krish', 'jack'],
            'City': ['London', 'Manchester', 'Liverpool', 'Bristol'],
            'Age': [20, 21, 19, 18],
            'Marks': [0.9, 0.8, 0.7, 0.6],
            'dob': pd.date_range('2020-02-24', periods=4, freq='T'),
            'sum(Age-Marks)': [20.9, 21.8, 19.7, 18.6],
            'prod(Age-Marks)': [18.0, 16.8, 13.299999999999999, 10.799999999999999],
            'mean(Age-Marks)': [10.45, 10.9, 9.85, 9.3],
            'std(Age-Marks)': [13.505739520663058, 14.28355697996826, 12.94005409571382, 12.303657992645928],
            'max(Age-Marks)': [20.0, 21.0, 19.0, 18.0],
            'min(Age-Marks)': [0.9, 0.8, 0.7, 0.6]
        }
    )

    # init params
    assert transformer.variables == ['Age', 'Marks']
    assert transformer.operations == ['sum', 'prod', 'mean', 'std', 'max', 'min']
    # fit params
    assert transformer.input_shape_ == (4, 5)
    assert transformer.combination_dict_ == {
        'sum(Age-Marks)': 'sum',
        'prod(Age-Marks)': 'prod',
        'mean(Age-Marks)': 'mean',
        'std(Age-Marks)': 'std',
        'max(Age-Marks)': 'max',
        'min(Age-Marks)': 'min'
    }
    # transform params
    pd.testing.assert_frame_equal(X, ref)


def test_MathematicalCombinator_SelectedVariables_OnlyOneFeature(dataframe_vartypes):
    with pytest.raises(KeyError):
        transformer = MathematicalCombinator(variables=['Age'])


def test_MathematicalCombinator_SelectedVariables_NonNumeric(dataframe_vartypes):
    transformer = MathematicalCombinator(variables=['Name', 'Age', 'Marks'])
    with pytest.raises(TypeError):
        X = transformer.fit_transform(dataframe_vartypes)


def test_MathematicalCombinator_SelectedVariables_OutsideDataset(dataframe_vartypes):
    transformer = MathematicalCombinator(variables=['FeatOutsideDataset', 'Age'])
    with pytest.raises(KeyError):
        X = transformer.fit_transform(dataframe_vartypes)


def test_MathematicalCombinator_SelectedOperations(dataframe_vartypes):
    transformer = MathematicalCombinator(math_operations=['sum', 'mean'])

    X = transformer.fit_transform(dataframe_vartypes)

    ref = pd.DataFrame.from_dict(
        {
            'Name': ['tom', 'nick', 'krish', 'jack'],
            'City': ['London', 'Manchester', 'Liverpool', 'Bristol'],
            'Age': [20, 21, 19, 18],
            'Marks': [0.9, 0.8, 0.7, 0.6],
            'dob': pd.date_range('2020-02-24', periods=4, freq='T'),
            'sum(Age-Marks)': [20.9, 21.8, 19.7, 18.6],
            'mean(Age-Marks)': [10.45, 10.9, 9.85, 9.3],
        }
    )

    # init params
    assert transformer.variables == ['Age', 'Marks']
    assert transformer.operations == ['sum', 'mean']
    # fit params
    assert transformer.input_shape_ == (4, 5)
    assert transformer.combination_dict_ == {
        'sum(Age-Marks)': 'sum',
        'mean(Age-Marks)': 'mean'
    }
    # transform params
    pd.testing.assert_frame_equal(X, ref)


def test_MathematicalCombinator_SelectedOperations_NewVariablesNames(dataframe_vartypes):
    transformer = MathematicalCombinator(
        math_operations=['sum', 'mean'],
        new_variables_names=['sum_of_two_vars', 'mean_of_two_vars']
    )

    X = transformer.fit_transform(dataframe_vartypes)

    ref = pd.DataFrame.from_dict(
        {
            'Name': ['tom', 'nick', 'krish', 'jack'],
            'City': ['London', 'Manchester', 'Liverpool', 'Bristol'],
            'Age': [20, 21, 19, 18],
            'Marks': [0.9, 0.8, 0.7, 0.6],
            'dob': pd.date_range('2020-02-24', periods=4, freq='T'),
            'sum_of_two_vars': [20.9, 21.8, 19.7, 18.6],
            'mean_of_two_vars': [10.45, 10.9, 9.85, 9.3],
        }
    )

    # init params
    assert transformer.variables == ['Age', 'Marks']
    assert transformer.operations == ['sum', 'mean']
    assert transformer.new_variables_names == ['sum_of_two_vars', 'mean_of_two_vars']
    # fit params
    assert transformer.input_shape_ == (4, 5)
    assert transformer.combination_dict_ == {
        'sum_of_two_vars': 'sum',
        'mean_of_two_vars': 'mean'
    }
    # transform params
    pd.testing.assert_frame_equal(X, ref)


def test_MathematicalCombinator_SelectedOperations_NewVariablesNames_LengthNotEqual(dataframe_vartypes):
    with pytest.raises(KeyError):
        transformer = MathematicalCombinator(
            math_operations=['sum', 'mean'],
            new_variables_names=['sum_of_two_vars', 'mean_of_two_vars', 'another_alias', 'not_permitted']
        )

    with pytest.raises(KeyError):
        transformer = MathematicalCombinator(
            math_operations=['sum', 'mean'],
            new_variables_names=['sum_of_two_vars']
        )

def test_MathematicalCombinator_SelectedoperationsOnlyOneOperation(dataframe_vartypes):
    # case 2: selected only one operation:
    transformer = MathematicalCombinator(math_operations=['sum'])

    X = transformer.fit_transform(dataframe_vartypes)

    ref = pd.DataFrame.from_dict(
        {
            'Name': ['tom', 'nick', 'krish', 'jack'],
            'City': ['London', 'Manchester', 'Liverpool', 'Bristol'],
            'Age': [20, 21, 19, 18],
            'Marks': [0.9, 0.8, 0.7, 0.6],
            'dob': pd.date_range('2020-02-24', periods=4, freq='T'),
            'sum(Age-Marks)': [20.9, 21.8, 19.7, 18.6]
        }
    )

    # init params
    assert transformer.variables == ['Age', 'Marks']
    assert transformer.operations == ['sum']
    # fit params
    assert transformer.input_shape_ == (4, 5)
    assert transformer.combination_dict_ == {
        'sum(Age-Marks)': 'sum'
    }
    # transform params
    pd.testing.assert_frame_equal(X, ref)


def test_MathematicalCombinator_SelectedoperationsOutsidePermittedList(dataframe_vartypes):
    with pytest.raises(KeyError):
        transformer = MathematicalCombinator(math_operations=['OperationOutsidePermittedList'])


def test_MathematicalCombinator_SelectedoperationsWrongType(dataframe_vartypes):
    with pytest.raises(KeyError):
        transformer = MathematicalCombinator(math_operations=[sum])
