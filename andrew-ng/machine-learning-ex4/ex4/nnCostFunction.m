function [J, grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
                               
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
 
% You need to return the following variables correctly 
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%

X = [ones(m, 1) X];

% Theta1    - 25 x 401
% X         - 5000 x 401
A2 = sigmoid(Theta1 * X');
A2 = [ones(1, size(A2, 2)); A2];

% Theta2    - 10 x 26
% A2        - 26 x 5000
A3 = sigmoid(Theta2 * A2);
A3 = A3';

% A3        - 5000 x 10
eye_matrix = eye(num_labels);
Y = eye_matrix(y,:);  

% Y         - 5000 x 10
A = -log(A3) .* Y;
B = -log(1 - A3) .* (1 - Y);

J = (sum(A(:)) + sum(B(:))) / m; 


% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%

% Theta1    - 25 x 401
% Theta2    - 10 x 26
% Y - 5000 x 10

a1 = X';                            % 401 x 5000
z2 = Theta1 * a1;                   % 25 x 5000
a2 = [ones(1, m); sigmoid(z2)];     % 26 x 5000
   
a3 = sigmoid(Theta2 * a2);   % 10 x 5000
delta3 = a3 - Y';            % 10 x 5000
    
delta2 = (Theta2(:,2:end)' * delta3) .* sigmoidGradient(z2);   % 25 x 5000
    
Theta1_grad = delta2 * a1';
Theta2_grad = delta3 * a2';
   
Theta1_grad = Theta1_grad / m;
Theta2_grad = Theta2_grad / m;

% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

Theta1(:, 1) = [];
Theta2(:, 1) = [];

Theta1_squared = Theta1.^2;
Theta2_squared = Theta2.^2;

J = J + lambda * (sum(Theta1_squared(:)) + sum(Theta2_squared(:))) / (2*m);

Theta1_grad(:,2:end) = Theta1_grad(:,2:end) + Theta1 * lambda / m;
Theta2_grad(:,2:end) = Theta2_grad(:,2:end) + Theta2 * lambda / m;


% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
