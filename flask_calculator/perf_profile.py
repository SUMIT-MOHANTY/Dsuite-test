#!/usr/bin/env python3
import cProfile
import pstats
from app import create_app

def performance_test():
    app = create_app()
    with app.test_client() as client:
        # Test basic operations
        for op in ['add', 'subtract', 'multiply', 'divide']:
            try:
                client.post('/calculate', data={
                    'num1': '10.5',
                    'num2': '5.2',
                    'operation': op
                })
            except:
                pass

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    performance_test()
    profiler.disable()
    
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)
