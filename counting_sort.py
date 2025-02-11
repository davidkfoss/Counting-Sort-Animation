from manim import *


class CountingSortAnimation(Scene):
    def construct(self):
        # Introduction sequence
        self.intro_sequence()
        self.wait(1)

        # Main sorting animation
        self.sorting_sequence()

    def intro_sequence(self):
        # Title
        title = Text("Understanding Counting Sort", color=BLUE).scale(1.2)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.scale(0.6).to_edge(UP))

        # Prerequisites text
        prereq_title = Text(
            "Before we begin, let's understand:", color=YELLOW).scale(0.8)
        prereq_title.next_to(title, DOWN, buff=0.8)

        prerequisites = VGroup(
            Text("1. We can only sort numbers (not letters or words)"),
            Text("2. Numbers must be positive integers (whole numbers)"),
            Text("3. We need to know the largest number in advance")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.6)
        prerequisites.next_to(prereq_title, DOWN, buff=0.5)

        self.play(Write(prereq_title))
        self.play(Write(prerequisites), run_time=2)
        self.wait(1)

        # How it works
        how_title = Text("How Counting Sort Works:", color=GREEN).scale(0.8)
        how_title.next_to(prerequisites, DOWN, buff=0.8)

        steps = VGroup(
            Text("1. Count how many times each number appears"),
            Text("2. Create an array to store these counts"),
            Text("3. Use the counts to place numbers in correct positions")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).scale(0.6)
        steps.next_to(how_title, DOWN, buff=0.5)

        self.play(Write(how_title))
        self.play(Write(steps), run_time=2)
        self.wait(1)

        # Example introduction
        example = Text("Let's see this in action with an example!",
                       color=BLUE).scale(0.7)
        example.next_to(steps, DOWN, buff=0.8)

        self.play(Write(example))
        self.wait(1)

        # Clear screen for main animation
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

    def sorting_sequence(self):
        # Initial array
        numbers = [4, 2, 2, 8, 3, 3, 1]
        max_val = max(numbers)

        # Create title
        title = Text("Counting Sort Visualization").scale(0.8)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(0.5)

        # Add explanation text
        explanation = Text("Starting with unsorted numbers:").scale(0.6)
        explanation.next_to(title, DOWN)
        self.play(Write(explanation))

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
        initial_array.next_to(explanation, DOWN, buff=0.7)

        # Label for initial array
        init_label = Text("Initial Array:").scale(0.6)
        init_label.next_to(initial_array, LEFT)

        self.play(
            Create(initial_squares),
            run_time=1
        )
        self.wait(0.3)
        self.play(
            Write(initial_nums),
            Write(init_label),
            run_time=1
        )
        self.wait(1)

        # Create count array with explanation
        count_explanation = Text(
            "Creating count array (index = number, value = frequency):").scale(0.6)
        count_explanation.next_to(initial_array, DOWN)
        self.play(Write(count_explanation))

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
        count_array.next_to(count_explanation, DOWN, buff=0.7)

        # Label for count array
        count_label = Text("Count Array:").scale(0.6)
        count_label.next_to(count_array, LEFT)

        self.play(
            Create(count_squares),
            run_time=1
        )
        self.wait(0.3)
        self.play(
            Write(count_nums),
            Write(count_indices),
            Write(count_label),
            run_time=1
        )
        self.wait(0.5)

        # Update count array with explanation
        counting_explanation = Text(
            "Counting frequency of each number:").scale(0.6)
        counting_explanation.next_to(count_array, DOWN)
        self.play(Write(counting_explanation))

        counts = [0] * (max_val + 1)
        for num in numbers:
            counts[num] += 1
            new_num = Text(str(counts[num]))
            new_num.move_to(count_nums[num])

            self.play(
                Flash(initial_nums[numbers.index(num)]),
                run_time=0.3
            )
            self.wait(0.2)

            self.play(
                Transform(count_nums[num], new_num),
                run_time=0.3
            )
            self.wait(0.3)

        self.wait(0.5)

        # Create output array with explanation
        output_explanation = Text(
            "Building sorted array using counts:").scale(0.6)
        output_explanation.next_to(counting_explanation, DOWN)
        self.play(Write(output_explanation))

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
        output_array.next_to(output_explanation, DOWN, buff=0.7)

        # Label for output array
        output_label = Text("Sorted Array:").scale(0.6)
        output_label.next_to(output_array, LEFT)

        self.play(
            Create(output_squares),
            Write(output_label),
            run_time=1
        )
        self.wait(0.5)

        idx = len(numbers) - 1
        for i in range(max_val, -1, -1):
            for _ in range(counts[i]):
                new_num = Text(str(i))
                new_num.move_to(output_squares[idx])

                self.play(
                    Flash(count_squares[i]),
                    run_time=0.3
                )
                self.wait(0.2)

                self.play(
                    Transform(output_nums[idx], new_num),
                    run_time=0.3
                )
                self.wait(0.2)
                idx -= 1

            if counts[i] > 0:
                self.wait(0.3)

        # Final explanation
        final_text = Text(
            "And we're done! The array is now sorted!", color=GREEN).scale(0.6)
        final_text.next_to(output_array, DOWN)
        self.play(Write(final_text))
        self.wait(1.5)


if __name__ == "__main__":
    config.quality = "medium_quality"
    config.frame_rate = 30
    config.pixel_height = 720
    config.pixel_width = 1280
