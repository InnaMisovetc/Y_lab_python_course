from task1.app.bruteforce import BruteForcePlanner, InputHandler


def main():
    planner = BruteForcePlanner(InputHandler.read_points())
    best_path = planner.find_best_path()
    print(best_path)
    planner.draw_path_planing()


if __name__ == '__main__':
    main()
