/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    now = 0
    next = 1
    while (true) {
        yield now
        c = now
        now = next
        next = now + c
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */