import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Company,
    DataSource,
    EmissionRecord
)

from .utils import (
    normalize_unit,
    detect_suspicious
)


class UploadCSVView(APIView):

    def post(self, request):

        file = request.FILES.get('file')

        if not file:
            return Response(
                {'error': 'No file uploaded'},
                status=status.HTTP_400_BAD_REQUEST
            )

        df = pd.read_csv(file)

        company, _ = Company.objects.get_or_create(
            name='Demo Company'
        )

        records_created = 0

        # =========================
        # SAP DATA
        # =========================
        if 'FuelType' in df.columns:

            source = DataSource.objects.create(
                company=company,
                source_type='SAP',
                file_name=file.name
            )

            for _, row in df.iterrows():

                normalized_value, normalized_unit = normalize_unit(
                    row['Quantity'],
                    row['Unit']
                )

                suspicious = detect_suspicious(
                    normalized_value
                )

                EmissionRecord.objects.create(
                    company=company,
                    source=source,

                    scope='SCOPE_1',

                    category='Fuel',

                    activity_type=row['FuelType'],

                    raw_value=row['Quantity'],
                    raw_unit=row['Unit'],

                    normalized_value=normalized_value,
                    normalized_unit=normalized_unit,

                    occurred_at=row['Date'],

                    status='PENDING',

                    is_suspicious=suspicious
                )

                records_created += 1

        # =========================
        # UTILITY DATA
        # =========================
        elif 'kWh' in df.columns:

            source = DataSource.objects.create(
                company=company,
                source_type='UTILITY',
                file_name=file.name
            )

            for _, row in df.iterrows():

                suspicious = detect_suspicious(
                    row['kWh']
                )

                EmissionRecord.objects.create(
                    company=company,
                    source=source,

                    scope='SCOPE_2',

                    category='Electricity',

                    activity_type=row['Tariff'],

                    raw_value=row['kWh'],
                    raw_unit='kWh',

                    normalized_value=row['kWh'],
                    normalized_unit='kWh',

                    occurred_at=row['BillingStart'],

                    status='PENDING',

                    is_suspicious=suspicious
                )

                records_created += 1

              # =========================
        # TRAVEL DATA
        # =========================
        elif 'DistanceKm' in df.columns:

            source = DataSource.objects.create(
                company=company,
                source_type='TRAVEL',
                file_name=file.name
            )

            for _, row in df.iterrows():

                suspicious = detect_suspicious(
                    row['DistanceKm']
                )

                EmissionRecord.objects.create(
                    company=company,
                    source=source,

                    scope='SCOPE_3',

                    category='Business Travel',

                    activity_type=row['TravelType'],

                    raw_value=row['DistanceKm'],
                    raw_unit='km',

                    normalized_value=row['DistanceKm'],
                    normalized_unit='km',

                    occurred_at='2026-01-01',

                    status='PENDING',

                    is_suspicious=suspicious
                )

                records_created += 1

        else:
            return Response(
                {'error': 'Unsupported CSV format'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({
            'message': 'CSV uploaded successfully',
            'records_created': records_created
        })
