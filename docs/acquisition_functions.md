Four different acquisitoin functions are used:

>Maximum Uncertainty (MU)  
>Maximum Expected Improvement (MEI)   
>Maximum Likelihood of Improvement (MLI)  
>Upper Confidence Bound (UCB)

<br>


**MU:**  
This function queries the sample with the highest uncertainty.
<br>
$$ x^* = arg\_max \enspace \sigma[f(x_i)]$$
<br>

<br>

**MEI:**  
This approach takes the maximum value of the prediction of the model over the possible experiments to run.

<br>

$$ x^* = arg\_max \enspace E[f(x_i)]$$

<br>

**MLI:**  
This approach tells us that we are expecting to query a region for which we see an improvement and sufficient uncertainty to have a high likelihood of getting a larger value.

$$ x^* = arg\_max \enspace \frac{E[f(x_i)] - E[f(x_{best})]}{\sigma[f(x_i)]}$$

$x_{best}$ is the current best value in the training dataset.


**UCB:**  
This strategy queries the sample with the maximum value of its mean prediction plus its uncertainty.
<br>
$$ x^* = arg\_max \enspace [E[f(x_i)] + \sigma[f(x_i)]]$$
<br>

$x^*$ is the new sample pulled using the acquistion function.  
$\sigma$ is the standard deviation ($\sigma^2$ is the variance)
$f(x_i)$ is the model and $x_i$ is a given predicted data point.  
$E[...]$ is the expected value.

