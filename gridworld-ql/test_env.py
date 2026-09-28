from environment import GridWorld

def test_top_wall():
    env = GridWorld()
    env.reset()
    s, r, done = env.step(0)
    assert s == [0, 0], f"FAIL: ky vong [0,0], nhan {s}"

def test_left_wall():
    env = GridWorld()
    env.reset()
    s, r, done = env.step(3)
    assert s == [0, 0], f"FAIL: Expectation [0,0], real {s}"

def test_bottom_wall():
    env = GridWorld()
    env.reset()
    s, r, done = env.step(1)
    assert s == [1, 0], f"FAIL: Expectation [1,0], real {s}"

def test_right_wall():
    env = GridWorld()
    env.reset()
    s, r, done = env.step(2)
    assert s == [0, 1], f"FAIL: Expectation [0,1], real {s}"

def test_goal():
    env = GridWorld()
    env.reset()
    s, _, _ = env.step(2)
    _, r, done = env.step(1)
    assert s == [3, 3], f"FAIL: Expectation [0,1], real {s}"
    assert done == True, f"FAIL: Expectation reach goal, real {done}"

def test_reset():
    env = GridWorld()
    env.step(3)
    s, r, done = env.reset() 
    assert s == [0, 0], f"FAIL: Expectation [0,0], real {s}"
