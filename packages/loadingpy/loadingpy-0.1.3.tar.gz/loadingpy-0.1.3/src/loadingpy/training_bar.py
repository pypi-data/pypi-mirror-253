from typing import Any, Iterable, Optional

from .alias import aliases
from .basic_bar import BarConfig
from .loading_bar import PyBar


@aliases("trainbar")
class TrainBar(PyBar):
    def __init__(
        self,
        iterable: Iterable,
        num_epochs: int,
        monitoring: Optional[Any] = None,
        naming: Optional[Any] = None,
        base_str: str = "loop",
        interpolation: int = 1,
        color: str = "green",
        frames_to_skip: int = 1,
        continuous_left_bar: bool = True,
    ) -> None:
        """
        creates a progress bar for a python iterable.

        Args:
            iterable: python object that can be iterated over
            num_epochs [int]: number of epochs for the first main progress bar
            monitoring [OPTIONAL]: a python object (or list of python objects) that will be printed after each iteration
                using the following format f'{monitoring}'. IF they are updated during the loop, make sure to
                update inplace, in order to see the changes
            naming [OPTIONAL]: if you want to add a descritpion prefix to the monitoring variables
            base_str [OPTIONAL]: prefix description of the loop we are iterating over
            interpolation [int]: interpolation polynomial degree for eta
            color [OPTIONAL]: which color to use for the loading bar
            frames_to_skip [Optional]: in order to avoid overloading the terminal with too many prompts,
                we can skip an number of frames
            continuous_left_bar: use a continuous epoch progress bar
        """
        self.raw_dataset = iterable
        self.frames_to_skip = frames_to_skip
        super().__init__(iterable, monitoring, naming, -1, base_str, interpolation, color)
        self.num_steps_per_epoch = self.total_steps
        self.total_steps = self.num_steps_per_epoch * num_epochs
        self.second_bar_length = int(2 * self.progress_bar_size / 5)
        self.progress_bar_size = self.progress_bar_size - self.second_bar_length
        self.num_epochs = num_epochs - 1
        self.curr_epoch = 0
        self.in_epoch_current_progression = 0
        self.continuous_left_bar = continuous_left_bar

    def build_prefix(self, progression_complete: bool) -> str:
        base_string = (
            super().build_prefix()
            + " "
            + self.build_bar(
                progression_complete=progression_complete,
                progress_bar_size=self.second_bar_length - 3,
                current_progression=self.current_progression if self.continuous_left_bar else self.curr_epoch,
                total_steps=max(1, self.total_steps if self.continuous_left_bar else self.num_epochs),
            )
        )
        return base_string

    def __next__(self, *args: Any, **kwds: Any) -> Any:
        progression_complete = (
            self.in_epoch_current_progression >= self.num_steps_per_epoch and self.curr_epoch == self.num_epochs
        )
        if self.in_epoch_current_progression >= self.num_steps_per_epoch:
            self.in_epoch_current_progression = 0
            self.curr_epoch += 1
        if (self.current_progression % self.frames_to_skip) == 0 or progression_complete:
            base_string = self.build_prefix(progression_complete=progression_complete)
            suffix = self.build_suffix(progression_complete=progression_complete)
            self.update_bar_size()
            main_bar = self.build_bar(
                progression_complete=self.in_epoch_current_progression >= self.num_steps_per_epoch - 1
                or progression_complete,
                progress_bar_size=self.progress_bar_size,
                current_progression=self.in_epoch_current_progression,
                total_steps=self.num_steps_per_epoch,
            )
            if not BarConfig["disable loading bar"]:
                print(
                    f"\r{base_string} {main_bar} {suffix}",
                    end="" if not progression_complete else "\n",
                )
        if progression_complete:
            raise StopIteration
        try:
            output = next(self.iterable)
        except StopIteration:
            self.iterable = iter(self.raw_dataset)
            output = next(self.iterable)
        self.current_progression += 1
        self.in_epoch_current_progression += 1
        return output
