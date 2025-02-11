from manim import *


class CountingSortAnimation(Scene):
    def construct(self):
        # Initial array
        numbers = [4, 2, 2, 8, 3, 3, 1]
        max_val = max(numbers)

        # Create title
        title = Text("Counting Sort Visualization").scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))

        # Create initial array visualization
        initial_squares = VGroup(*[
            Square(side_length=0.8).set_fill(BLUE, opacity=0.5)
            for _ in numbers
        ]).arrange(RIGHT, buff=0.2)

        initial_nums = VGroup(*[
            Text(str(num)).move_to(square)
            for num, square in zip(numbers, initial_squares)
        ])

        initial_array = VGroup(initial_squares, initial_nums)
        initial_array.next_to(title, DOWN, buff=1)

        # Label for initial array
        init_label = Text("Initial Array:").scale(0.6)
        init_label.next_to(initial_array, LEFT)

        self.play(
            Create(initial_squares),
            Write(initial_nums),
            Write(init_label)
        )
        self.wait()

        # Create count array
        count_squares = VGroup(*[
            Square(side_length=0.8).set_fill(GREEN, opacity=0.3)
            for _ in range(max_val + 1)
        ]).arrange(RIGHT, buff=0.2)

        count_nums = VGroup(*[
            Text("0").move_to(square)
            for square in count_squares
        ])

        count_indices = VGroup(*[
            Text(str(i), color=RED).scale(0.6).next_to(square, DOWN, buff=0.2)
            for i, square in enumerate(count_squares)
        ])

        count_array = VGroup(count_squares, count_nums, count_indices)
        count_array.next_to(initial_array, DOWN, buff=1.5)

        # Label for count array
        count_label = Text("Count Array:").scale(0.6)
        count_label.next_to(count_array, LEFT)

        self.play(
            Create(count_squares),
            Write(count_nums),
            Write(count_indices),
            Write(count_label)
        )
        self.wait()

        # Update count array
        counts = [0] * (max_val + 1)
        for num in numbers:
            counts[num] += 1
            new_num = Text(str(counts[num]))
            new_num.move_to(count_nums[num])
            self.play(
                Transform(count_nums[num], new_num),
                Flash(initial_nums[numbers.index(num)]),
                run_time=0.5
            )
        self.wait()

        # Create output array
        output = [0] * len(numbers)
        output_squares = VGroup(*[
            Square(side_length=0.8).set_fill(YELLOW, opacity=0.3)
            for _ in numbers
        ]).arrange(RIGHT, buff=0.2)

        output_nums = VGroup(*[
            Text("").move_to(square)
            for square in output_squares
        ])

        output_array = VGroup(output_squares, output_nums)
        output_array.next_to(count_array, DOWN, buff=1.5)

        # Label for output array
        output_label = Text("Sorted Array:").scale(0.6)
        output_label.next_to(output_array, LEFT)

        self.play(
            Create(output_squares),
            Write(output_label)
        )

        # Fill output array
        idx = len(numbers) - 1
        for i in range(max_val, -1, -1):
            for _ in range(counts[i]):
                new_num = Text(str(i))
                new_num.move_to(output_squares[idx])
                self.play(
                    Transform(output_nums[idx], new_num),
                    Flash(count_squares[i]),
                    run_time=0.5
                )
                idx -= 1

        # Final pause
        self.wait(2)


if __name__ == "__main__":
    config.quality = "medium_quality"
    config.frame_rate = 30
    config.pixel_height = 720
    config.pixel_width = 1280
