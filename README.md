# Counting Inversions

## Complexity

- Best: O(n log n)
- Worst: O(n log n)
- Avg: O(n log n)
- Space: O(n)

## Problem Description

Counting inversions measures how far an array is from being sorted. An inversion is a pair of indices `i < j` such that `S[i] > S[j]`. In other words, the earlier value is larger than a later value even though those two elements should appear in the opposite order in a sorted array.

This makes inversion counting a useful way to describe how mixed up a sequence is. A perfectly sorted array has zero inversions, while a reverse-sorted array has the maximum possible number. The challenge is to count all of those out-of-order pairs efficiently without comparing every possible pair one at a time.

## Code

```javascript
/**
 * Merge two sorted halves while counting cross inversions.
 *
 * @param {number[]} left Left sorted half.
 * @param {number[]} right Right sorted half.
 * @returns {{sorted: number[], inversions: number}} Merged output and inversion count.
 */
function mergeAndCount(left, right) {
    let leftIndex = 0;
    let rightIndex = 0;
    let sortedArray = [];
    let inversions = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] <= right[rightIndex]) {
            sortedArray.push(left[leftIndex]);
            leftIndex++;
        } else {
            sortedArray.push(right[rightIndex]);
            // Every remaining left value forms an inversion with right[rightIndex].
            inversions += left.length - leftIndex;
            rightIndex++;
        }
    }

    sortedArray = sortedArray
        .concat(left.slice(leftIndex))
        .concat(right.slice(rightIndex));

    return { sorted: sortedArray, inversions };
}

/**
 * Count inversions in an array with a merge-sort-style divide-and-conquer approach.
 *
 * @param {number[]} values Input array.
 * @returns {{sorted: number[], inversions: number}} Sorted array and total inversion count.
 */
function countingInversions(values) {
    if (values.length <= 1) {
        return { sorted: values, inversions: 0 };
    }

    const mid = Math.floor(values.length / 2);
    const leftHalf = countingInversions(values.slice(0, mid));
    const rightHalf = countingInversions(values.slice(mid));
    const mergedResult = mergeAndCount(leftHalf.sorted, rightHalf.sorted);

    return {
        sorted: mergedResult.sorted,
        // Add inversions from both halves and from pairs that cross the midpoint.
        inversions:
            leftHalf.inversions +
            rightHalf.inversions +
            mergedResult.inversions,
    };
}

/**
 * Run the counting-inversions demonstration.
 *
 * @returns {void}
 */
function main() {
    const array = [42, 7, 91, 18, 63, 25, 4, 77, 56, 13];
    const result = countingInversions(array);

    console.log("Original array =", array);
    console.log("Sorted array =", result.sorted);
    console.log("Inversion count =", result.inversions);
}

main();
```

## Algorithm Steps

1. Split the array recursively until each subarray has length 0 or 1.
2. Count the inversions in the left half.
3. Count the inversions in the right half.
4. Merge the two sorted halves back together.
5. Whenever a value from the right half is placed before the remaining values in the left half, add the number of unmerged left values to the inversion count.
6. Add the left, right, and cross-half inversion counts to obtain the final answer.

## Explanation

This implementation uses the same divide-and-conquer structure as merge sort. The array is split into two halves, each half is processed recursively, and then the two sorted halves are merged back together. That structure is important because it lets the algorithm count inversions in three parts: inversions entirely in the left half, inversions entirely in the right half, and inversions that cross from the left half to the right half.

The merge step is where the main idea appears. If the next value to place comes from the right half before the current value from the left half, then that right-half value is smaller than not just one left value, but every remaining value in the left half. So instead of counting those inversions one at a time, the algorithm adds all of them in a single step. That is what makes the method much faster than the brute-force `O(n^2)` approach.

In the JavaScript version, `slice()` is used to create the smaller recursive halves, and `concat()` is used when the merge step finishes building the combined sorted array. The function also returns an object with both the sorted result and the inversion count, which keeps the recursive return values organized while the algorithm combines the left, right, and cross-half counts.

Because each recursive level performs linear merge work and there are `log n` levels, the total runtime is `O(n log n)`. The implementation also uses `O(n)` extra space for the merged arrays that are created while the recursion combines results.
