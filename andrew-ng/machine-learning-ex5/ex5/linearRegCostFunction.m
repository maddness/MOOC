function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
%J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%


A = sum((X * theta - y).^2);

theta_squared = theta .^2;
Rj = lambda / (2*m) * sum(theta_squared(2:length(theta)));

J = A / (2*m) + Rj;


Rd = lambda / m * theta;
Rd(1) = 0;
G = X' * (X*theta - y);

grad = G / m + Rd;







% =========================================================================

grad = grad(:);

end
