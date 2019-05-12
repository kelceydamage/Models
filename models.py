#!/usr/bin/env python
# ------------------------------------------------------------------------ 79->
# Author: ${name=Kelcey Damage}
# Python: 3.5+
# Doc
#
# REDCAPE
# ------------------------------------------------------------------------ 79->
# Dependancies:
#

# Imports
# ------------------------------------------------------------------------ 79->

# Globals
# ------------------------------------------------------------------------ 79->

# Classes
# ------------------------------------------------------------------------ 79->
class CommonNumericArrayFunctions():

    def averageOfArray(self, array):
        return sum(array) / len(array)

class InputValidation():
    # Common validation to raise exceptions and avoid undefined errors.

    def isOddNumber(self, number):
        if number % 2 == 0:
            return False
        return True

    def isBinaryIntegerArray(self, array):
        if all(True if x == 1 or x == 0 else False for x in array):
            return True
        return False

    def isNumericArray(self, array):
        if all(True if isinstance(x, int) or isinstance(x, float) else False for x in array):
            return True
        return False

    def acceptArrayOfOddLenth(self, array):
        if not self.isOddNumber(len(array)):
            raise Exception("List must contain an odd amount of elements")

    def acceptArrayOfBinaryIntegers(self, array):
        if not self.isBinaryIntegerArray(array):
            raise Exception("List contains non-binary or boolean values")

    def acceptArrayOfNumbers(self, array):
        if not self.isNumericArray(array):
            raise Exception("List contains non-numeric values")

    def acceptNumericValue(self, value):
        if not isinstance(value, int) or isinstance(value, float):
            raise Exception("Value is non-numeric")

    def acceptEquality(self, a, b):
        if not a == b:
            raise Exception("Values are not equal")


class CondorcetJuryTheorem(InputValidation):
    """
    ---------------------------------------------------------------------- 79->
    NAME:
            Condorcet Jury Theorem

    CLASS/INVOCATION:
            CondorcetJuryTheorem().run(binaryIntegerArray)
    
    DESCRIPTION:
            Each of an odd number of models classifies an unknown state of the 
            world as either true or false. Each model classifies correctly with 
            a probability of p > 0.5, and the probability that any model 
            classifies correctly is statistically independent of the 
            correctness of any other model.

            A majority vote classifies correctly with higher probability than 
            any one model, and as the number of models become large, the 
            accuracy of the majority vote approaches 100%.

    RETURNS:
            A boolean representing the majority vote. To achieve True, there 
            must be a greater number of 1's than 0's in the binary array.
                - vote
    """

    def __init__(self):
        self.vote = False

    def _validateInputs(self, binaryIntegerArray):
        self.acceptArrayOfOddLenth(binaryIntegerArray)
        self.acceptArrayOfBinaryIntegers(binaryIntegerArray)

    def _tallyVotes(self):
        if self.binaryIntegerArray.count(1) > self.noOfVotes // 2:
            self.vote = True

    def run(self, binaryIntegerArray):
        self._validateInputs(binaryIntegerArray)
        self.binaryIntegerArray = binaryIntegerArray
        self.noOfVotes = len(binaryIntegerArray)
        self._tallyVotes()
        return self.vote


class DiversityPredictionTheorem(InputValidation, CommonNumericArrayFunctions):
    """
    ---------------------------------------------------------------------- 79->
    NAME:
            Diversity Prediction Theorem

    CLASS/INVOCATION:
            DiversityPredictionTheorem().run(predictionArray, trueValue)
    
    DESCRIPTION:
            Many-Model Error equals Average Model Error minus Diveristy of 
            Model Predictions.

            This is an equality. 

    RETURNS:
            A tuple of three float values in the following order:
                - averageModelError
                - diversityOfModelPredictions
                - manyModelError
    """

    def __init__(self):
        self.precision = 6

    def _validateInputs(self, predictedArray, observedValue):
        self.acceptArrayOfNumbers(predictedArray)
        self.acceptNumericValue(observedValue)

    def _averageModelError(self):
        self.averageModelError = round(
            sum(
                (predictedValue - self.observedValue) ** 2 / self.noOfPredictions
                for predictedValue in self.predictedArray
            ), 
            self.precision
        )

    def _diversityOfModelPredictions(self):
        self.diversityOfModelPredictions = round(
            sum(
                (predictedValue - self.averagePredictedValue) ** 2 / self.noOfPredictions
                for predictedValue in self.predictedArray
            ),
            self.precision
        )

    def _manyModelError(self):
        self.manyModelError = round(
            (self.averagePredictedValue - self.observedValue) ** 2,
            self.precision
        )

    def _testEquality(self):
        E1 = self.manyModelError
        E2 = round(
            self.averageModelError - self.diversityOfModelPredictions, 
            self.precision
            )
        if E1 != E2:
            e = "Unknown error equality does not match: {0} != {1}".format(E1, E2)
            raise Exception(e)

    def run(self, predictedArray, observedValue):
        self._validateInputs(predictedArray, observedValue)
        self.predictedArray = predictedArray
        self.observedValue = observedValue
        self.noOfPredictions = len(predictedArray)
        self.averagePredictedValue = self.averageOfArray(predictedArray)
        self._averageModelError()
        self._diversityOfModelPredictions()
        self._manyModelError()
        self._testEquality()
        return (
            self.averageModelError,
            self.diversityOfModelPredictions,
            self.manyModelError
        )


class RSquared(InputValidation, CommonNumericArrayFunctions):
    """
    ---------------------------------------------------------------------- 79->
    NAME:
            R^2: Percentage Of Variance

    CLASS/INVOCATION:
            RSquared().run(observedArray, predictedArray)
    
    DESCRIPTION:
            the proportion of the variance for a dependent variable that's 
            explained by an independent variable or variables in a regression 
            model

            Also calculates residuals

    RETURNS:
            A float between 0 and 1 representing the percentage of explained 
            variance.
                - coefficientOfDetermination

            Optional: self.residuals, returns a list of residuals.
    """

    def __init__(self):
        pass

    def _validateInputs(self, observedArray, predictedArray):
        self.acceptEquality(len(observedArray), len(predictedArray))
        self.acceptArrayOfNumbers(observedArray)
        self.acceptArrayOfNumbers(predictedArray)

    def _totalSumOfSquares(self):
        self.totalSumOfSquares = sum(
            (observedValue - self.averageOfObservedValues) ** 2 
            for observedValue in self.observedArray
        )

    def _regressionSumOfSquares(self):
        self.regressionSumOfSquares = sum(
            (predictedValue - self.averageOfObservedValues) ** 2 
            for predictedValue in self.predictedArray
        )

    def _residualSumOfSquares(self):
        self.residuals = [
            predictedValue - observedValue
            for predictedValue, observedValue in zip(
                self.predictedArray,
                self.observedArray
            )
        ]
        self.residualSumOfSquares = sum(
            residual ** 2 for residual in self.residuals
            )

    def _coefficientOfDetermination(self):
        self.coefficientOfDetermination = 1 - (
            self.residualSumOfSquares / self.totalSumOfSquares
        )

    def run(self, observedArray, predictedArray):
        self._validateInputs(observedArray, predictedArray)
        self.observedArray = observedArray
        self.predictedArray = predictedArray
        self.averageOfObservedValues = self.averageOfArray(observedArray)
        self._totalSumOfSquares()
        self._regressionSumOfSquares()
        self._residualSumOfSquares()
        self._coefficientOfDetermination()
        return self.coefficientOfDetermination
        

class ModelErrorDecompositionTheorem(InputValidation, CommonNumericArrayFunctions):
    """
    ---------------------------------------------------------------------- 79->
    NAME:
            Model Error Decomposition Theorem

    CLASS/INVOCATION:
            
    
    DESCRIPTION:
           

    RETURNS:
            
    """


# Functions
# ------------------------------------------------------------------------ 79->
def documentation():
    print(CondorcetJuryTheorem.__doc__)
    print(DiversityPredictionTheorem.__doc__)
    print(RSquared.__doc__)
    print(ModelErrorDecompositionTheorem.__doc__)


# Main
# ------------------------------------------------------------------------ 79->
if __name__ == '__main__':
    documentation()
    Model = DiversityPredictionTheorem()
    print(Model.run([2,5,4,9,2,1,4,3,3], 4))
    Model = CondorcetJuryTheorem()
    print(Model.run([0,1,0,0,1,1,0]))
    Model = RSquared()
    print(Model.run([1,3,2,5,4,8,5,7], [1,2,3,4,5,6,7,8]))
    print(Model.residuals)
    
 