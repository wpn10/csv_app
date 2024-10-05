import csv
import io
import re
from collections import defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentData
from .serializers import StudentDataSerializer

class CSVUploadView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({"error": "File is required."}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['file']

        try:
            data_set = file.read().decode('utf-8-sig')
            io_string = io.StringIO(data_set)
            csv_reader = csv.DictReader(io_string)
        except Exception as e:
            return Response({"error": f"Error reading CSV file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        fieldnames = [field.strip() for field in csv_reader.fieldnames]

        if 'First Name' not in fieldnames or 'Last Name' not in fieldnames:
            return Response({"error": "CSV must contain 'First Name' and 'Last Name' columns."}, status=status.HTTP_400_BAD_REQUEST)

        other_fields = [field for field in fieldnames if field not in ['First Name', 'Last Name']]

        pattern = re.compile(r'^(?P<base>.+?)\s*(?P<number>\d+)$')

        base_fields = defaultdict(list)
        for field in other_fields:
            match = pattern.match(field)
            if match:
                base = match.group('base').strip()
                base_fields[base].append(field)
            else:
                base_fields[field].append(field)

        records = []
        for row in csv_reader:
            first_name = row.get('First Name', '').strip()
            last_name = row.get('Last Name', '').strip()
            name = f"{first_name} {last_name}".strip()

            base_data = {'name': name}

            dynamic_fields = {k: v for k, v in base_fields.items() if len(v) > 1}
            static_fields = {k: v for k, v in base_fields.items() if len(v) == 1}

            max_instances = max([len(v) for v in dynamic_fields.values()], default=1)

            for i in range(max_instances):
                data = base_data.copy()
                additional_data = {}

                for base, columns in static_fields.items():
                    column = columns[0]
                    value = row.get(column, '').strip()
                    additional_data[base] = value

                for base, columns in dynamic_fields.items():
                    if i < len(columns):
                        column = columns[i]
                        value = row.get(column, '').strip()
                        additional_data[base] = value
                    else:
                        additional_data[base] = ''

                data['additional_data'] = additional_data
                records.append(data)

        serializer = StudentDataSerializer(data=records, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentListView(APIView):
    def get(self, request):
        students = StudentData.objects.all()
        serializer = StudentDataSerializer(students, many=True)
        data = []
        for item in serializer.data:
            combined_data = {key: item[key] for key in item if key != 'additional_data'}
            additional_data = item.get('additional_data') or {}
            combined_data.update(additional_data)
            data.append(combined_data)
        return Response(data, status=status.HTTP_200_OK)

