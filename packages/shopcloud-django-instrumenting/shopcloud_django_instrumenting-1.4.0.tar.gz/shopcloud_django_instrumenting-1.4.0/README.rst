Instrumenting
=============

install
-------

-  install with your favorite Python package manager

.. code:: sh

   pip3 install shopcloud-django-instrumenting

LogRequestMiddleware
~~~~~~~~~~~~~~~~~~~~

add additional Information from request in AppEngine to Log

usage
^^^^^

add to MIDDLEWARE in django-app settings.py:

.. code:: python

   MIDDLEWARE = [
       ...
       'shopcloud_django_instrumenting.middleware.LogRequestMiddleware',
   ]

tracing
-------

.. code:: py

   from shopcloud_django_instrumenting import tracing

   tr = tracing.Tracer('name_of_service', 'name_of_operation')
   with tr.start_span('event.processing') as span:
       pass

   data = tr.close()


Error Management
----------------

A special layer on top of the API is the error boundary within the with blocks of spans. This layer catches exceptions and prints them. The pattern here is to catch all runtime errors and return a 422 status, indicating that an unexpected error has occurred, not a validation error. If you need to return validation data to the user, you must return a Result object on your own.

.. code-block:: python

   @action(detail=True, methods=["post"], url_path="my-action")
   def my_action(self, request, pk):
      tr = tracing.DjangoAPITracer(request)

      serializer = serializers.ProductSyncSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)

      with tr.start_span('proceed') as span:
         raise Exception('something unhandled')

      trace_data = tr.close()
      return Response({
         'trace': trace_data,
      }, status=status.HTTP_201_CREATED if tr.is_success else status.HTTP_422_UNPROCESSABLE_ENTITY)

Another pattern to note is that every `with` block should contain a repeatable operation. You can create structures where you can run blocks side by side and only repeat some of them. However, be careful: while the `with` block catches exceptions, it may not guarantee that all variables are set.

.. code-block:: python

   tr = tracing.DjangoAPITracer(request)

   is_a_success = False
   is_b_success = False
   is_c_success = False

   with tr.start_span('A') as span_a:
      is_a_success = False

   with tr.start_span('B') as span_b:
      is_b_success = True

   with tr.start_span('C') as span_c:
      if is_a_success:
         pass

develop
-------

.. code:: sh

   $ pytest
   $ pip3 install coverage
   # shell report
   $ coverage run -m pytest  && coverage report --show-missing
   # html report
   $ coverage run -m pytest  && coverage html
   $ cd htmlcov
   $ python3 -m http.server
