import setuptools

if __name__ == '__main__':
    setuptools.setup( install_requires=[
          'rich',
          'fastapi',
          'fastapi_limiter',
          'redis',
          'aioredis',
          'uvicorn'
      ])
