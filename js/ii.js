/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
const insert = function (intervals, newInterval) {
  const result = []

  let index = 0
  while (index < intervals.length && intervals[index][0] < newInterval[0]) {
    result.push(intervals[index++])
  }

  if (result.length === 0 || result[result.length - 1][1] < newInterval[0]) {
    result.push(newInterval)
  } else {
    result[result.length - 1][1] = Math.max(result[result.length - 1][1], newInterval[1])
  }

  while (index < intervals.length) {
    const  interval = intervals[index++]
    if (result[result.length - 1][1] < interval[0]) {
      result.push(interval)
    } else {
      result[result.length - 1][1] = Math.max(result[result.length - 1][1], interval[1])
    }
  }

  return result
}
