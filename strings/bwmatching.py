# python3
import sys

# BWTを入力として、元の文字列でパターンにマッチする位置を返す
def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  Symbols = ['A', 'C', 'G', 'T', '$']
  L = len(bwt)
  first_column = sorted(bwt)
  last_column = bwt

  starts = {}
  occ_count_before = {}
  count = {}

  for s in Symbols:
    starts[s] = -1
    count[s] = 0
    occ_count_before[s] = [0 for i in range(L+1)]

  for i in range(L):
    c = first_column[i]
    if starts[c] < 0:
      starts[c] = i

    c = last_column[i]
    count[c] += 1
    for s in Symbols:
      occ_count_before[s][i+1] = count[s]

  return (starts, occ_count_before)


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  top = 0
  bottom = len(bwt) - 1
  while top <= bottom:
    if len(pattern) > 0:
      c = pattern[-1]
      pattern = pattern[:-1]

      top = starts[c] + occ_counts_before[c][top]
      bottom = starts[c] + occ_counts_before[c][bottom+1] - 1
    else:
      return bottom - top + 1

  return 0
     

if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
