import cProfile
import pstats
import io
from app import create_app

def profile_app():
    app = create_app()
    pr = cProfile.Profile()
    pr.enable()
    
    # Simulate a request
    with app.test_client() as client:
        client.post('/calculate', data={
            'num1': '100',
            'num2': '200',
            'operation': 'add'
        })
    
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats(10)
    print("Performance Profile:\n", s.getvalue())

if __name__ == '__main__':
    profile_app()
