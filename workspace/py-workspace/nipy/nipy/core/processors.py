from nipy.db.mongo_state import write_state, read_state


def run_always(func):
    def wrapper():
        while True:
            func()
    return wrapper


def processor(in_queue, out_queue, read, write):
    def decorator(process):
        @run_always
        def wrapper():
            unit = read(in_queue)
            result = process(unit)
            write(out_queue, result)
        return wrapper
    return decorator


def state_processor(in_queue, out_queue, read, write):
    def decorator(process):
        @run_always
        def wrapper():
            unit = read(in_queue)
            state = read_state(in_queue)
            unit_result, state_result = process(unit, state)
            write_state(in_queue, state_result)
            write(out_queue, unit_result)
        return wrapper
    return decorator
