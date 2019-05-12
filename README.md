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


    ---------------------------------------------------------------------- 79->
    NAME:
            Model Error Decomposition Theorem

    CLASS/INVOCATION:


    DESCRIPTION:


    RETURNS:
