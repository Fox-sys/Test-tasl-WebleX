import traceback


class BaseTest:
    def get_test_name(self):
        raise NotImplementedError

    def get_tests(self):
        raise NotImplementedError

    def do_job(self):
        print(f'Test {self.get_test_name()}')
        success = 0
        failed = 0
        errors = 0

        for test in self.get_tests():
            try:
                test()
                success += 1
            except AssertionError:
                failed += 1
                print(test.__name__, '- failed')
            except:
                errors += 1
                print(traceback.format_exc())

        print(f'success: {success}, failed: {failed}, errors: {errors}')