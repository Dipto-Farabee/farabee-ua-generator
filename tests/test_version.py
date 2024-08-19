"""
Random User-Agent
Copyright: 2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import unittest

import src.ua_generator as ua_generator
from src.ua_generator.data.version import Version, WindowsVersion, AndroidVersion, ChromiumVersion, VersionRange
from src.ua_generator.options import Options


class TestVersion(unittest.TestCase):
    def test_version(self):
        version = Version(major=1, minor=2, build=3, patch=4)
        self.assertEqual(version.format(), '1.2.3.4')
        self.assertEqual(version.format(partitions=4), '1.2.3.4')
        self.assertEqual(version.format(partitions=3), '1.2.3')
        self.assertEqual(version.format(partitions=2), '1.2')
        self.assertEqual(version.format(partitions=1), '1')
        self.assertEqual(version.to_tuple(), (1, 2, 3, 4))

    def test_version_2(self):
        version = Version(major=1, minor=2, build=3, patch=None)
        self.assertEqual(version.format(), '1.2.3')
        self.assertEqual(version.format(partitions=4), '1.2.3.0')
        self.assertEqual(version.format(partitions=3), '1.2.3')
        self.assertEqual(version.format(partitions=2), '1.2')
        self.assertEqual(version.format(partitions=1), '1')
        self.assertEqual(version.to_tuple(), (1, 2, 3, 0))

    def test_version_3(self):
        version = Version(major=1, minor=2, build=None, patch=0)
        self.assertEqual(version.format(), '1.2.0.0')
        self.assertEqual(version.format(partitions=4), '1.2.0.0')
        self.assertEqual(version.format(partitions=3), '1.2.0')
        self.assertEqual(version.format(partitions=2), '1.2')
        self.assertEqual(version.format(partitions=1), '1')
        self.assertEqual(version.to_tuple(), (1, 2, 0, 0))

    def test_version_4(self):
        version = Version(major=1, minor=2, patch=4)
        self.assertEqual(version.format(), '1.2.0.4')
        self.assertEqual(version.format(partitions=4), '1.2.0.4')
        self.assertEqual(version.format(partitions=3), '1.2.0')
        self.assertEqual(version.format(partitions=2), '1.2')
        self.assertEqual(version.format(partitions=1), '1')
        self.assertEqual(version.to_tuple(), (1, 2, 0, 4))

    def test_version_5(self):
        version = Version(major=0, build=3)
        self.assertEqual(version.format(), '0.0.3')
        self.assertEqual(version.format(partitions=4), '0.0.3.0')
        self.assertEqual(version.format(partitions=3), '0.0.3')
        self.assertEqual(version.format(partitions=2), '0.0')
        self.assertEqual(version.format(partitions=1), '0')
        self.assertEqual(version.to_tuple(), (0, 0, 3, 0))

    def test_version_6(self):
        version = Version(major=1, minor=2)
        self.assertEqual(version.format(), '1.2')
        self.assertEqual(version.format(partitions=3), '1.2.0')
        self.assertEqual(version.to_tuple(), (1, 2, 0, 0))

    def test_version_7(self):
        version = Version(major=1)
        self.assertEqual(version.format(), '1')
        self.assertEqual(version.format(partitions=2), '1.0')
        self.assertEqual(version.to_tuple(), (1, 0, 0, 0))

    def test_version_separator(self):
        version = Version(major=1, minor=2, build=3, patch=4)
        self.assertEqual(version.format(separator='_'), '1_2_3_4')
        self.assertEqual(version.format(partitions=4, separator='_'), '1_2_3_4')
        self.assertEqual(version.format(partitions=3, separator='_'), '1_2_3')
        self.assertEqual(version.format(partitions=2, separator='_'), '1_2')
        self.assertEqual(version.format(partitions=1, separator='_'), '1')

    def test_version_separator_2(self):
        version = Version(major=1, minor=2, build=3, patch=None)
        self.assertEqual(version.format(separator='_'), '1_2_3')
        self.assertEqual(version.format(partitions=4, separator='_'), '1_2_3_0')
        self.assertEqual(version.format(partitions=3, separator='_'), '1_2_3')
        self.assertEqual(version.format(partitions=2, separator='_'), '1_2')
        self.assertEqual(version.format(partitions=1, separator='_'), '1')

    def test_version_separator_3(self):
        version = Version(major=1, minor=2, build=3, patch=0)
        self.assertEqual(version.format(separator='_'), '1_2_3_0')
        self.assertEqual(version.format(partitions=4, separator='_'), '1_2_3_0')
        self.assertEqual(version.format(partitions=3, separator='_'), '1_2_3')
        self.assertEqual(version.format(partitions=2, separator='_'), '1_2')
        self.assertEqual(version.format(partitions=1, separator='_'), '1')

    def test_version_trim_zero(self):
        version = Version(major=1, minor=2, build=0, patch=0)
        self.assertEqual(version.format(trim_zero=True), '1.2')

    def test_version_trim_zero_2(self):
        version = Version(major=1, minor=2, build=0, patch=4)
        self.assertEqual(version.format(trim_zero=True), '1.2.0.4')

    def test_version_trim_zero_3(self):
        version = Version(major=1, minor=None, build=3, patch=4)
        self.assertEqual(version.format(partitions=2, trim_zero=True), '1')

    def test_version_range(self):
        version = Version(build=(90, 100))
        self.assertTrue(version.build >= 90 and version.build <= 100)

    def test_version_windows(self):
        version = WindowsVersion(version=Version(major=10, minor=0), ch_platform=Version(major=1, minor=2))
        self.assertEqual(version.format(partitions=4), '10.0.0.0')
        self.assertEqual(version.ch_platform.format(partitions=4), '1.2.0.0')

    def test_version_windows_range(self):
        version = WindowsVersion(version=Version(major=10, minor=0), ch_platform=Version(major=(1, 10)))
        self.assertEqual(version.format(partitions=4), '10.0.0.0')
        self.assertTrue(version.ch_platform.major >= 1 and version.ch_platform.major <= 10)

    def test_version_android(self):
        version = AndroidVersion(version=Version(major=14, minor=0, build=0), build_numbers=('foo', 'foo'))
        self.assertEqual(version.format(partitions=4), '14.0.0.0')
        self.assertEqual(version.build_number, 'foo')

    def test_version_chromium(self):
        version = ChromiumVersion(Version(major=1, minor=2, build=3, patch=4), webkit=Version(537, 36))
        self.assertEqual(version.format(partitions=4), '1.2.3.4')
        self.assertEqual(version.webkit.format(), '537.36')

    def test_version_comparison(self):
        version_1 = Version(major=1, minor=2)
        version_2 = Version(major=1, minor=3)
        self.assertFalse(version_1 == version_2)
        self.assertTrue(version_1 != version_2)
        self.assertTrue(version_1 < version_2)
        self.assertFalse(version_1 > version_2)
        self.assertTrue(version_1 <= version_2)
        self.assertFalse(version_1 >= version_2)

    def test_version_comparison_2(self):
        version_1 = Version(major=1, minor=0)
        version_2 = Version(major=1, minor=0)
        self.assertTrue(version_1 == version_2)
        self.assertFalse(version_1 != version_2)
        self.assertFalse(version_1 < version_2)
        self.assertFalse(version_1 > version_2)
        self.assertTrue(version_1 <= version_2)
        self.assertTrue(version_1 >= version_2)

    def test_version_VersionRange(self):
        version_range = VersionRange(1, 2)
        self.assertIsNotNone(version_range)
        self.assertIsNotNone(version_range.min_version)
        self.assertIsNotNone(version_range.max_version)
        self.assertIsInstance(version_range.min_version, Version)
        self.assertIsInstance(version_range.max_version, Version)
        self.assertEqual(version_range.min_version.format(), Version(1).format())
        self.assertEqual(version_range.max_version.format(), Version(2).format())
        self.assertEqual(version_range.min_version.to_tuple(), Version(1).to_tuple())
        self.assertEqual(version_range.max_version.to_tuple(), Version(2).to_tuple())
        self.assertEqual(version_range.min_version.format(partitions=4), '1.0.0.0')
        self.assertEqual(version_range.max_version.format(partitions=4), '2.0.0.0')
        self.assertTrue(version_range.max_version.to_tuple() > version_range.min_version.to_tuple())

    def test_version_VersionRange_2(self):
        version_range = VersionRange(Version(major=100, minor=0, build=2), 101)
        self.assertIsNotNone(version_range)
        self.assertIsNotNone(version_range.min_version)
        self.assertIsNotNone(version_range.max_version)
        self.assertIsInstance(version_range.min_version, Version)
        self.assertIsInstance(version_range.max_version, Version)
        self.assertEqual(version_range.min_version.format(), Version(major=100, minor=0, build=2).format())
        self.assertEqual(version_range.max_version.format(), Version(101).format())
        self.assertEqual(version_range.min_version.to_tuple(), Version(major=100, minor=0, build=2).to_tuple())
        self.assertEqual(version_range.max_version.to_tuple(), Version(101).to_tuple())
        self.assertEqual(version_range.min_version.format(partitions=4), '100.0.2.0')
        self.assertEqual(version_range.max_version.format(partitions=4), '101.0.0.0')
        self.assertTrue(version_range.max_version.to_tuple() > version_range.min_version.to_tuple())

    def test_version_VersionRange_3(self):
        # MUST be valid version range
        chrome_min = 124
        chrome_max = 127

        for i in range(0, 100):
            options = Options(
                selected_versions={
                    'chrome': VersionRange(min_version=chrome_min, max_version=chrome_max),
                })
            ua = ua_generator.generate(browser='chrome', options=options)
            self.assertTrue(ua.browser == 'chrome')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(chrome_min <= ua.generator.browser_version.major <= chrome_max)

    def test_version_VersionRange_4(self):
        # MUST be valid version range
        firefox_min = 125
        firefox_max = 129

        for i in range(0, 100):
            options = Options(selected_versions={
                'firefox': VersionRange(min_version=firefox_min, max_version=firefox_max),
            })
            ua = ua_generator.generate(browser='firefox', options=options)
            self.assertTrue(ua.browser == 'firefox')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertTrue(firefox_min <= ua.generator.browser_version.major <= firefox_max)

    def test_version_VersionRange_multiple(self):
        # MUST be valid version range
        chrome_min = 124
        chrome_max = 127
        firefox_min = 125
        firefox_max = 129

        for i in range(0, 100):
            options = Options(selected_versions={
                'chrome': VersionRange(min_version=chrome_min, max_version=chrome_max),
                'firefox': VersionRange(min_version=firefox_min, max_version=firefox_max),
            })
            ua = ua_generator.generate(browser=('chrome', 'firefox'), options=options)
            self.assertIn(ua.browser, ('chrome', 'firefox'))
            self.assertIsNotNone(ua.generator.browser_version)
            if ua.browser == 'chrome':
                self.assertTrue(chrome_min <= ua.generator.browser_version.major <= chrome_max)
            if ua.browser == 'firefox':
                self.assertTrue(firefox_min <= ua.generator.browser_version.major <= firefox_max)

    def test_version_VersionRange_5(self):
        # MUST be valid version range
        macos_min = 12
        macos_max = 14

        for i in range(0, 100):
            options = Options(selected_versions={
                'macos': VersionRange(min_version=macos_min, max_version=macos_max),
            })
            ua = ua_generator.generate(platform='macos', options=options)
            self.assertTrue(ua.platform == 'macos')
            self.assertIsNotNone(ua.generator.platform_version)
            self.assertTrue(macos_min <= ua.generator.platform_version.major <= macos_max)

    def test_version_VersionRange_invalid(self):
        # MUST be INVALID version range
        edge_min = 1
        edge_max = 2

        for i in range(0, 100):
            options = Options(selected_versions={
                'edge': VersionRange(min_version=edge_min, max_version=edge_max),
            })
            ua = ua_generator.generate(browser='edge', options=options)
            self.assertTrue(ua.browser == 'edge')
            self.assertIsNotNone(ua.generator.browser_version)
            self.assertFalse(edge_min <= ua.generator.browser_version.major <= edge_max)


if __name__ == '__main__':
    unittest.main()
