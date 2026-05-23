function func() {
  try {
    console.log(1)
    return 
  } catch (e) {
    console.log(2)
  } finally {
    console.log(3)
  }
  console.log(4)
}

func()

// 1
// 3