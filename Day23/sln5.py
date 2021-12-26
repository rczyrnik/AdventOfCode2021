# import utils


DEBUG = False

TARGET_ROOM_X = [2, 4, 6, 8]
COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}
ROOM_MARKERS = ["A", "B", "C", "D"]
ALLOWED_HALL_SPOTS = [0, 1, 3, 5, 7, 9, 10]

ROOM_MARKER_X = {marker: x for marker, x in zip(ROOM_MARKERS, TARGET_ROOM_X)}
ROOM_MARKER_IDX = {marker: idx for marker, idx in zip(ROOM_MARKERS, range(4))}

HALLWAY_MARKER = "H"

TERMINAL_PT1 = tuple(tuple(ROOM_MARKERS[i] for _ in range(2)) for i in range(4))
TERMINAL_PT2 = tuple(tuple(ROOM_MARKERS[i] for _ in range(4)) for i in range(4))
EMPTY_HALLWAY = tuple(None for _ in range(11))

COST_MAP = {(EMPTY_HALLWAY, TERMINAL_PT1): 0, (EMPTY_HALLWAY, TERMINAL_PT2): 0}
BEST_MOVES = {}


def moveable_pods(hallway, rooms):
    moveable = []
    # only move from room to hallway or hallway to room
    for k, v in enumerate(hallway):
        if v is None:
            continue
        target_room = rooms[ROOM_MARKER_IDX[v]]
        if not can_enter(target_room, v):
            continue
        tgt = ROOM_MARKER_X[v]
        if tgt > k and not hallway_blocked(k + 1, tgt, hallway):
            moveable.append((HALLWAY_MARKER, k, v))
        elif tgt < k and not hallway_blocked(tgt, k - 1, hallway):
            moveable.append((HALLWAY_MARKER, k, v))
    # Always do a hallway move if possible
    if moveable:
        return moveable
    for i, room in enumerate(rooms):
        room_x = TARGET_ROOM_X[i]
        if hallway[room_x - 1] is not None and hallway[room_x + 1] is not None:
            continue
        if all(pod is None or pod == ROOM_MARKERS[i] for pod in room):
            # If this room can be filled, then nobody needs to leave
            continue
        idx, pod = first_pod_in_room(room)
        moveable.append((i, idx, pod))
    return moveable


def hallway_blocked(p1, p2, hallway):
    s = min(p1, p2)
    d = max(p1, p2)
    return any(hallway[k] is not None for k in range(s, d + 1))


def can_enter(room, room_marker):
    return all(pod is None or pod == room_marker for pod in room) and any(
        pod is None for pod in room
    )


def first_pod_in_room(room):
    for i in range(len(room)):
        if room[i] != None:
            return i + 1, room[i]
    return None, None


def move_candidates(pod, hallway, rooms):
    # Returns list of all places a pod can move to, and how many steps it would take to get there
    pos_marker, idx, room_marker = pod
    room_idx = ROOM_MARKER_IDX[room_marker]
    if pos_marker == HALLWAY_MARKER:
        room = rooms[room_idx]
        room_x = TARGET_ROOM_X[room_idx]
        if can_enter(rooms[room_idx], room_marker):
            room_steps = max(i + 1 for i in range(len(room)) if room[i] is None)
            dist_to_room = abs(idx - TARGET_ROOM_X[room_idx])
            return [(room_idx, room_steps, (dist_to_room + room_steps))]
        else:
            return []
    else:
        # If currently in a room, make sure it's not the room we want to be in
        if pos_marker == room_idx and can_enter(rooms[room_idx], room_marker):
            return []

        possible_hallway_locs = []
        room_x = TARGET_ROOM_X[pos_marker]
        for k in ALLOWED_HALL_SPOTS:
            if hallway_blocked(room_x, k, hallway):
                if k > room_x:
                    break
                else:
                    continue
            dist_to_hall_pos = abs(room_x - k)
            possible_hallway_locs.append((HALLWAY_MARKER, k, idx + dist_to_hall_pos))
        return possible_hallway_locs


def move(hallway, rooms):
    if COST_MAP.get((hallway, rooms)) is not None:
        return COST_MAP.get((hallway, rooms))
    moveable = moveable_pods(hallway, rooms)
    if DEBUG:
        print(hallway, "\n", rooms, "\n", moveable)

    best_cost = float("inf")
    best_move = None
    for pod in moveable:
        pos_marker, pos_index, pod_marker = pod
        new_hallway = None
        new_rooms = None
        if pos_marker == HALLWAY_MARKER:
            assert pos_index in ALLOWED_HALL_SPOTS
            assert hallway[pos_index] == pod_marker
            new_hallway = utils.tuple_replace(hallway, pos_index, None)
        else:
            assert rooms[pos_marker][pos_index - 1] == pod_marker
            new_room = utils.tuple_replace(rooms[pos_marker], pos_index - 1, None)
            new_rooms = utils.tuple_replace(rooms, pos_marker, new_room)
        dest_candidates = move_candidates(pod, hallway, rooms)
        for dest in dest_candidates:
            dest_marker, dest_pos, steps_taken = dest
            if dest_marker == HALLWAY_MARKER:
                assert dest_pos in ALLOWED_HALL_SPOTS
                assert hallway[dest_pos] is None, (hallway, dest_pos)
                new_hallway = utils.tuple_replace(hallway, dest_pos, pod_marker)
            else:
                assert rooms[dest_marker][dest_pos - 1] is None, (rooms, dest)
                new_room = utils.tuple_replace(
                    rooms[dest_marker], dest_pos - 1, pod_marker
                )
                new_rooms = utils.tuple_replace(rooms, dest_marker, new_room)

            new_cost = move(new_hallway, new_rooms)
            move_cost = (COSTS[pod_marker] * steps_taken) + new_cost
            if move_cost < best_cost:
                best_move = (new_hallway, new_rooms)
                best_cost = move_cost
    COST_MAP[(hallway, rooms)] = best_cost
    if best_move is not None:
        BEST_MOVES[(hallway, rooms)] = best_move
    return best_cost


def unfold_rooms(rooms):
    ROOM_MIDDLE = [("D", "D"), ("C", "B"), ("B", "A"), ("A", "C")]
    new_rooms = tuple(
        (tup[0], ROOM_MIDDLE[i][0], ROOM_MIDDLE[i][1], tup[1])
        for i, tup in enumerate(rooms)
    )
    return new_rooms


def compact(state, cost):
    hallway, rooms = state
    hallway_str = "".join(" " if v is None else v for v in hallway)
    room_str = "][".join(
        "".join(" " if v is None else v for v in room) for room in rooms
    )
    return hallway_str, f"[{room_str}]", cost


def print_moves(hallway, rooms):
    state = (hallway, rooms)
    buf = []
    while True:
        buf.append(compact(state, COST_MAP[state]))
        state = BEST_MOVES.get(state)
        if state is None:
            break
    for mov in buf:
        print(mov)

def read_data(file_name):
	file = open(file_name, 'r')
	raw_lines = file.readlines()
	file.close()
	return [line.strip() for line in raw_lines]

# input_data = utils.get_input(day=23).strip().split("\n")
input_data = read_data('input3.txt')
parsed = [row[3:].strip().split("#", maxsplit=3) for row in input_data[2:4]]

print("Part 1")
rooms = tuple(tuple(j[i][0] for j in parsed) for i in range(4))
print(move(EMPTY_HALLWAY, rooms))
print_moves(EMPTY_HALLWAY, rooms)
print("*" * 80)

print("Part 2")
unfolded_rooms = unfold_rooms(rooms)
print(move(EMPTY_HALLWAY, unfolded_rooms))
print_moves(EMPTY_HALLWAY, unfolded_rooms)

