from environment import GridWorld

def test_top_wall():
    env = GridWorld()
    env.current = [0,1]
    s, r, done = env.step(0)
    assert s == [0, 1], f"FAIL: ky vong [0,0], nhan {s}"
    assert r == -10 
    assert done == False


def test_left_wall():
    env = GridWorld()
    env.current = [1,0]
    s, r, done = env.step(3)
    assert s == [1, 0], f"FAIL: Expectation [0,0], real {s}"
    assert r == -10 
    assert done == False

def test_bottom_wall():
    env = GridWorld()
    env.current = [3,0]
    s, r, done = env.step(1)
    assert s == [3, 0], f"FAIL: Expectation [1,0], real {s}"
    assert r == -10 
    assert done == False

def test_right_wall():
    env = GridWorld()
    env.current = [0,3]
    s, r, done = env.step(2)
    assert s == [0, 3], f"FAIL: Expectation [0,1], real {s}"
    assert r == -10 
    assert done == False

def test_goal():
    env = GridWorld()
    env.current = [2,3]
    s, r, done = env.step(1)
    assert done == True, f"FAIL: Expectation reach goal, real {s}"
    assert s == [3,3]
    assert r == 9

def test_reset():
    env = GridWorld()
    env.start = [2,2]
    env.current = [1,1]
    env.reset() 
    assert env.current == [2, 2]

def test_step():
    env = GridWorld()
    env.current = [2,3]
    s, r, done = env.step(3)
    assert done == False
    assert s == [2,2]
    assert r == -1

