## Cross product

- Given vectors [1, 2, 3] and [2, 3, 4] and assuming each pair is x, y, z correspondingly, the cross product is simply:

[1]   [2] -> x
[2] * [3] -> y
[3]   [4] -> z
	
For x = (2 * 4) - (3 * 3)
For y = - ((1 * 4) - (2 * 3) # I don't know what the minus is for but it always is there
For z = the same but excluding z

The result is a vector of the same length as the intial two vectors but perpendicular (orthogonal) to both vectors.

It's just an X multiplication excluding the variable you're defining. Why is this useful? Because the cross product is completely unrelated (uncorrelated) to the initial
two vectors. For example, for estimating Principal Component Analysis the algorithm calculates a latent variable unrelated to all input variables.

- Cross product is anticommutative, which means that the order matters, in this case changing the order results on vectors having opposite directions.
