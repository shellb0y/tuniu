from multiprocessing import Pool
import os, time, random
import requests
import base_data


def task(name):
    print '[%s] Run task %s (%s)...' % (time.time(), name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


def http_task(NO):
    url = "http://120.26.213.143:8002/api/checkcode/dcc"

    sessionid = base_data.get_random_letter_number()
    payload = "sessionid=" + sessionid + "&data=FZGH65jOwHBapPa74KyMYN9eSJeLKdGZSTxvimqel4zyRjaFq4VJmRq%2BHs7prGd9ghVlNcsFMCw615EthQkMOh4oBmBkfXplVOEH%2FhZH8pmw6kHB1uc%2FPFDgjUs%2Fkz8pgFa9laRc6b0txyvQi8M2o3b9j5wpdl3qBzTs%2F10KoKAOPyL9ZHdwiQ8Qk90VhkuK%2BGA6YulsLYKYN6XPThQSezCA0zad6xcqlfQ3DfEva9TehLThPSTuxk7dINflthe2HpXOlafYxay6d5%2F7AfUZjlB%2F4vZJh1j%2FTZo8%2Fo0DjfkgY%2BUivCC7FQVajEECemfzJWRiQmPzq4JSMmvF4j4vb0e1077FXl5vvm8sqI11YTKeYEjXjYLHFfrMsN4jWNahhgO5KZm4r3tKAVj86lM1SISWdWYBDfZgniiyiprhzkc3SqoXzXATWT7KptZ8C2J8mQNwmAGrRWBeraG63zmxv06uzyz2oLI3AM%2FzDA8GsKdkDmmti7N6SFJGmg3ExBqug0JZ4QZecuTcbfcPYPP208NWHrQ73pBo3w4hnConCSdb0tHJba3PGt6MI38rduCt3IcFQh5Bmz30MP5MjXbUlM3d9Jhxm0cClK2fhysCCiIemlEOVbsWrfCUkcyX0G5XVcGsGTz%2FptUlAYrsBSLq49BCfvzGUzsXMIpdgcEBIs8ZJH52LV94ZD5efmC1ZVdTHR01ggogU4SpxPprPLcjUVNwMTCskPvozDZc7Nu%2BU0Ajbpd%2FbYfo5NxGlgZIAJo4%2BBU1m0vpXgzEVh4zlhtdhxlJqfFUkjVzIcMc0WiPSBYQgzIx%2Bquw98k0AaaNc4A09VEZZW99mwm%2B4xcUaOKLY2C5C7dN4I9alfdGfE43UWTmC%2B9bK%2BsxedvQaWa1Eit9Kp2t8EttA4%2BeiS4qHr5CUnjNo5sBlJCNt05vxBuW1X774WI%2BRx0IwksXXt%2Bgdlsxo30fzOciSkJj7djfU%2FujbmJ4XodNKffltZWiTrQ5e6IwMzHkg%2Bb8fwY7YbOCWNM23r4eDftUYhj6ME5SLJrN4bu7gjuMqU1mmMB%2FIzDV2wnWvWWZZXD087ISnwI4w%2Fto1YD7MHWgUC7Ovp4YIVDFv8ua4vcWPsJUNjxJFWfrPQ1gwCTxaMWjRbpo3Ec5nnmncvnDt4u4OrbgOi0jFcZX%2Bpatp8iZqjnCA%2BImoEgRP0GJcMZ7rfEQqGtNGWlhepygZ%2BnaZgyELeHDCvh32dYUFjSaWr2EFeUJ472i8xVpBquZ9ZCks7Q9zfbpYTeYsWXMoCcOdqzXoq6QNszT1gczOjzbHl9ZTc3gAMkDru0nfK%2BXB84EUsBgWhvowk%2BhKJcbkCTfEuRM5UAntrDbUm%2Fhyyb516v5X6N9ugaYDyBXbm5cBEpk7hbLtIb9ONDpkJhPzFycoH8wrxlOpR134%2BKcBu8v%2FAqbG3%2F4PW3ligXWCje4IkdDB3zoJjLHWG9Vv7hREjhE1frkx8uooAwRMFs%2FibnYu5%2FwaqhZLjubxJD8fBezXRJ1F5susWtLW1vzP914NdWO3beX8iza9dsvVsfUwDiWY6heN2W%2FtrzebaJTcwOjp0C7pGKnOiyUVTJn8dbAiPZ%2Fzysby465SttCwhQKkn3G0n2eYQcO13gNEERYhCMOVNpcHNsHnhNGBB7EuH1IR7kuR5UKtbCKuQihMM2nk5%2BoTVxRbfBp5hrGbryFUiL5p0raNg4iXJI5p02Bnpf2NrddLnKgFHPGkx%2Fbhrs2NYmTWW92JHkxUUXoukoxQsjkEIyDzj4g0O9Aa2LdhUkMO%2BqbHlGOp%2Bwziirl8pemaigwiYTQHSXk7ayC9m%2FB9J76zqZ6yx3OF7hjvSzR0PQfZ%2FxzQBkxPsnflzOKL%2B0u%2BSWyPPajV%2BEiQbiye%2FzcZ42%2F%2B89VHnQG0faoMjA%2BUlNvDwSUeaf3Q5PgF7%2BA1hawq0riktZeUoPNJuFdN5mZ7ZfPoC4HQJrGZV7raJRYFYmgyFk0uqLF6fhVwnwNmu8nwPrErjJHJC2b1i23MEDNcNDCr2WyAqdsig%2FTBGIbiEcNiC7brjZG%2BdbTUV0hIwMpq7cvtbsZTJfzWgRBfu56d%2B5i%2Bs46bH9OzSJ1NYo%2BlpDEmU6u4eX8M7Qscya7KNV0OuTwDdRz5myKBLlAMrQKNBAl7TNXtYzCxhWOfOHPwUxendz2f0vOX8ULNO5WhLyao9%2BE3bz4We%2FoVU0M1vTCnkxoX55JrpXHftru4FOOyECOoYMomi6quuDniDe53Ew0E0A6dUEuaQEAKQaP08SIuVNdhF6cgfxLEa%2Fkk3ePHTYwoJqzwX4bIQJoJ7LCUTSx2Zp0k3a5G3vlcYNLzr25gsYCDUuCbuTXbeoXlMtK6CNIc9QOEJ%2FcoQyNv9D0KRWw%2B2zJ%2BxquYNzB%2FDpH1VS2iGTJK%2Br7gkIxZUBHIGmPA6QZGrGXGjjE%2BrQGEfmRdFKqoQ6mpVT6q3UBDkq5cJosbYrvHhztchteYB0OEtMnE0auTiiz06osZ%2BeRipw1Sg3rdoGzDQDKLVALM0V6OK96QWOBaTmB6es7nEbHy23%2BqA4Ie6bYkyrlF8Znfla%2BUuu9gMPPiONqteuxOirKbu%2Bov4h%2BkwSlHfFmYxsDv%2BnxH9xmnC3GKdcHrUCCn9AquswtHt0%2FtOQSnKip2s31hz5LmtF1mX%2Fw8C1EoFnFcyEmZVSWZ%2FEwaOlDQtj3AlM2eF6DNsA%2BGGfKLDV4MAG6jfue%2BSaxpEikjC95xolPv%2FuR7kesGF8h60xEgndUI53Ur0apyVB5B6%2BT5xiAVImuQzfZTmRhYj%2BZHx23uQQ1jVQFSxXFEAC19OXfGJvyeNONWt%2BcXSStODv9MU9lT5%2FDruwszx1iWkYh8FyUJI4tbIqxUmVTdx8UZehWWVlEGJc%2FbJ%2BiXDPqBB%2F2u2vx91tncpSPDXEUFOqSYQStXQteIoFs9%2FBbh5g2k8AvzfQHbxdlO9UA3%2FuI7P7GAoVeaCBBQE63NNhGG1xS416fkwtCwXzm%2FgW4Tbk23k01ALIJrKNdNmlr6%2Fnr4aocGVPJmsW7mhLczVhlVX%2B4Uy61wlmwALYBXv6ecQ8yjiDFx50dAPT5Ccra79OMkdsJ7RivG7xu%2BJDh20U%2FLC5qU4nmfjd8%2FZIIZbLEc%2F4OHe9E9mNr3LEov9YTJyMjkfKcTu9kI0zEPKxBYopt8vWgIZTPeqAGwvf1QIFbpimG7X4651bvh6Iy%2Bq%2B7smLKmsTlW0RpvDLG%2F%2Fs7bcC8eywG%2BzIh1PgdRyOGuDJaQpX%2FallLQvkbUrmptpJLgf3heRb8L8Cukay3%2FnlVB%2F5xYnOW%2Bhhz2ND3t3T7MqD6IzlqXlZXFjCZVzgg1eMiIJbi7LaMPQY0%2FFr9yqLAIVh9dNQtsVpJp1%2BfANleczg9YLzv4IIGwD50p3kK6CM8ZwRj3bYzwZT1aZ6ZsBnEik%2Fb47gwZjkeTh%2FdDsFTIOt9sM3ZkyTyXr3aLgbdm6iIzrDHeozMuUOvczOQKKMqOOgzi8r%2F7zG0f6EPVLStCMUdZ"
    headers = {
        'cache-control': "no-cache",
        'postman-token': "95694e79-d52d-306c-d259-4996794fbcff",
        'content-type': "application/x-www-form-urlencoded"
    }

    log = '#%d\t%d\t\t%s\t' % (NO, os.getpid(), time.time())
    start = time.time()
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.text == 'accept':
        log = log + str(round(time.time() - start, 2)) + 's\t'
    else:
        log = log + 'Nil'

    url = "http://120.26.213.143:8002/api/checkcode/" + sessionid
    for i in range(10):
        response = requests.request("GET", url)
        ret = response.text
        if ret:
            log += str(round(time.time() - start, 2)) + 's'
            break
        time.sleep(1)

    print log


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    print 'NO.\tpid\t\t\ttime\t\t\taccpet\tget_result'
    p = Pool(80)
    for i in range(80):
        p.apply_async(http_task, args=(i,))
    # print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'

    # for i in range(5):
    #     print i

    # http_task(1)
