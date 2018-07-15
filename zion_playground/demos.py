


DEMOS = [
    {
        "title": "Hello World",
        "slug": "hello-world",
        "program": '''
module _

fn main() {
    print("Hello Zion!")
}
''',
    },
    {
        "title": "8 Queens",
        "slug": "eight-queens",
        "program": '''
module _

fn queens(rows int, columns int) [[int]] {
    var solutions [[int]]
    var solution [int]

    # Introduce an empty solution upon which the dynamic programming algorithm can build
    append(solutions, solution)

    for row in range(rows) {
        solutions = add_one_queen(row, columns, solutions)
    }

    return solutions
}

fn add_one_queen(new_row int, columns int, prev_solutions [[int]]) [[int]] {
    var solutions [[int]]
    reserve(solutions, 92)

    for solution in prev_solutions {
        for new_column in range(columns) {
            if no_conflict(new_row, new_column, solution) {
                append(solutions, copy(solution, new_column))
            }
        }
    }

    return solutions
}

fn no_conflict(new_row int, new_column int, solution [int]) bool {
    for row in range(new_row) {
        condition := (
            solution[row]       != new_column           and
            solution[row] + row != new_column + new_row and
            solution[row] - row != new_column - new_row)
                        
        if not condition {
            return false
        }
    }

    return true
}

fn main() {
    solutions := queens(8, 8)

    for solution in solutions {
        print(solution)
    }
}
'''
    },
    {
        "title": "Basic functional programming",
        "slug": "basic-functional-programming",
        "program": '''
module _

fn square[T](x T) T {
  return x * x
}

fn apply[T](f (fn(T) T), x T) T {
  return f(x)
}

fn map[T](f (fn(T) T), xs [T]) [T] {
  var ys [T]
  for x in xs {
    append(ys, f(x))
  }
  return ys
}

fn filter[T](f (fn(T) bool), xs [T]) [T] {
  var ys [T]
  for x in xs {
    if f(x) {
      append(ys, x)
    }
  }
  return ys
}

fn reduce[S,X](f (fn(S, X) S), xs [X], initial S) S {
  var state = initial
  for x in xs {
    state = f(state, x)
  }
  return state
}

fn main() {
    print(square(3))
    print(apply(square, 2))
    print(filter(fn(x int) bool { return x > 5}, [1, 3, 5, 7, 9]))
    print(map(square, [1, 2, 3, 4]))
    print(reduce(fn(acc int, x int) { return acc + x }, [1, 2, 3, 4], 0))
}
'''
    },
]

DEMOS_BY_SLUG = {d['slug']: d for d in DEMOS}
