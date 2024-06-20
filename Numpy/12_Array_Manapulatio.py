import numpy as np

# Reshape -> change the shape of data
arr = np.array([[1, 2, 3], [4, 5, 6]])
new_arr = arr.reshape((3, 2))
print("Reshape:\n", new_arr)

# Flat  ->  create a 1-d iterator for n-d array
flat_iter = arr.flat
print("\nFlat:")
for item in flat_iter:
    print(item, end='  ')
print()
# Flatten  ->  Returns a copy of the array collapsed into one dimension
flat_arr = arr.flatten()
print("\nFlatten:\n", flat_arr)

# Ravel  ->  Returns a contiguous flattened array.
ravel_arr = arr.ravel() 
print("\nRavel:\n", ravel_arr)

# Transpose  -> transpose the array  mxn -> nxm
transposed_arr = arr.transpose()
print("\nTranspose:\n", transposed_arr)

# Rollaxis  ->  Rolls the specified axis backwards.
rolled_arr = np.rollaxis(arr, 0, 2)
print("\nRollaxis:\n", rolled_arr)

# Swapaxes  ->  Interchanges the two axes of an array.
swapped_arr = np.swapaxes(arr, 0, 1)
print("\nSwapaxes:\n", swapped_arr)

# Broadcast  ->  Produces an object that mimics broadcasting
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
broadcasted_arr = np.broadcast_to(arr1, (3, 3))
print("\nBroadcast:\n", broadcasted_arr)

# Broadcast_to -> Produces an object that mimics broadcasting
broadcasted_arr = np.broadcast_to(arr1, (3, 3))
print("\nBroadcast_to:\n", broadcasted_arr)

# Expand_dims  -> Expands the shape of an array.
expanded_arr = np.expand_dims(arr1, axis=0)
print("\nExpand_dims:\n", expanded_arr)

# Squeeze  ->  Removes single-dimensional entries from the shape of an array.
arr = np.array([[[1, 2, 3]]])
squeezed_arr = np.squeeze(arr)
print("\nSqueeze:\n", squeezed_arr)

# Concatenate  -> Joins a sequence of arrays along an existing axis.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated_arr = np.concatenate((arr1, arr2), axis=0)
print("\nConcatenate:\n", concatenated_arr)

# Stack  ->  Joins a sequence of arrays along a new axis.
stacked_arr = np.stack((arr1, arr2), axis=0)
print("\nStack:\n", stacked_arr)

# Hstack  ->  Stacks arrays in sequence horizontally (column wise).
stacked_arr = np.hstack((arr1[:, np.newaxis], arr2[:, np.newaxis]))
print("\nHstack:\n", stacked_arr)

# Vstack  ->  Stacks arrays in sequence vertically (row wise).
stacked_arr = np.vstack((arr1, arr2))
print("\nVstack:\n", stacked_arr)

# Split  ->  Splits an array into multiple sub-arrays.
arr = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr, 3)
print("\nSplit:\n", split_arr)

# Hsplit  -> Splits an array into multiple sub-arrays horizontally (column-wise).
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
split_arr = np.hsplit(arr, 3)
print("\nHsplit:\n", split_arr)

# Vsplit -> Splits an array into multiple sub-arrays vertically (row-wise).
split_arr = np.vsplit(arr, 2)
print("\nVsplit:\n", split_arr)

# Resize  ->  Returns a new array with the specified shape.
arr = np.array([[1, 2, 3], [4, 5, 6]])
resized_arr = np.resize(arr, (2, 3))
print("\nResize:\n", resized_arr)

# Append  ->  Appends the values to the end of an array.
arr = np.array([1, 2, 3])
arr = np.append(arr, [4, 5, 6])
print("\nAppend:\n", arr)

# Insert  -> Inserts the values along the given axis before the given indices.
arr = np.array([1, 2, 3, 4, 5])
arr = np.insert(arr, 2, [6, 7])
print("\nInsert:\n", arr)

# Delete  ->  Returns a new array with sub-arrays along an axis deleted.
arr = np.array([[1, 2, 3], [4, 5, 6]])
deleted_arr = np.delete(arr, 0, 0)
print("\nDelete:\n", deleted_arr)

# Unique  ->  Finds the unique elements of an array.
arr = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5])
unique_arr = np.unique(arr)
print("\nUnique:\n", unique_arr)