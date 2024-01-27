import functools
import re

version_patt = re.compile(r"^(\d+)\.(\d+)\.(\d+)(-(.+))?")


@functools.total_ordering
class Version:
    def __init__(self, string: str):
        m = version_patt.match(string)
        if not m:
            raise ValueError(f"{string} is not a valid version")
        self._x = int(m.group(1))
        self._y = int(m.group(2))
        self._z = int(m.group(3))
        self._suffix = m.group(5)

    def __repr__(self):
        v = f"{self._x}.{self._y}.{self._z}"
        return v if not self._suffix else f"{v}-{self._suffix}"

    def __eq__(self, other):
        return self._x == other._x \
            and self._y == other._y \
            and self._z == other._z \
            and self._suffix == other._suffix

    def __lt__(self, other):
        """
        >>> Version('1.1.1') < Version('1.1.2')
        True
        >>> Version('1.1.1') < Version('1.2.1')
        True
        >>> Version('1.1.1') < Version('2.1.1')
        True
        >>> Version('1.1.1') < Version('1.1.1')
        False
        >>> strings = ['10.0.0', '10.0.1', '1.10.10', '1.1.1-SNAPSHOT', '9.9.9', '1.1.1']
        >>> vs = [Version(s) for s in strings]
        >>> max(vs)
        10.0.1
        >>> min(vs)
        1.1.1-SNAPSHOT
        """
        if self._x < other._x: return True
        if self._x > other._x: return False

        if self._y < other._y: return True
        if self._y > other._y: return False

        if self._z < other._z: return True
        if self._z > other._z: return False

        if not self._suffix and other._suffix: return False
        if self._suffix and not other._suffix: return True
        if not self._suffix and not other._suffix: return False
        return self._suffix < other._suffix

    def is_snapshot(self):
        """
        >>> Version("1.1.1").is_snapshot()
        False
        >>> Version("1.1.1-SNAPSHOT").is_snapshot()
        True
        """
        return self._suffix is not None and "SNAPSHOT" in self._suffix

    @staticmethod
    def is_valid(string):
        """Check if a string is a valid version number

        >>> test="1.1.1"
        >>> missing_one = [test[:i] + test[i + 1:] for i in range(len(test))]
        >>> all(not Version.is_valid(tc) for tc in missing_one)
        True
        >>> valid_strings = ["1.2.3", "20.50.1", "1.1.000-ASDF"]
        >>> all(Version.is_valid(tc) for tc in valid_strings)
        True
        """
        return version_patt.match(string) is not None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
