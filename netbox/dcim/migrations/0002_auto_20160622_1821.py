# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 18:21
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0001_initial'),
        ('ipam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='primary_ip',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_for', to='ipam.IPAddress', verbose_name=b'Primary IP'),
        ),
        migrations.AddField(
            model_name='device',
            name='rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='devices', to='dcim.Rack'),
        ),
        migrations.AddField(
            model_name='consoleserverporttemplate',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cs_port_templates', to='dcim.DeviceType'),
        ),
        migrations.AddField(
            model_name='consoleserverport',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cs_ports', to='dcim.Device'),
        ),
        migrations.AddField(
            model_name='consoleporttemplate',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='console_port_templates', to='dcim.DeviceType'),
        ),
        migrations.AddField(
            model_name='consoleport',
            name='cs_port',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='connected_console', to='dcim.ConsoleServerPort', verbose_name=b'Console server port'),
        ),
        migrations.AddField(
            model_name='consoleport',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='console_ports', to='dcim.Device'),
        ),
        migrations.AlterUniqueTogether(
            name='pod',
            unique_together=set([('site', 'name'), ('site', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='rack',
            unique_together=set([('site', 'facility_id'), ('site', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='powerporttemplate',
            unique_together=set([('device_type', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='powerport',
            unique_together=set([('device', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='poweroutlettemplate',
            unique_together=set([('device_type', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='poweroutlet',
            unique_together=set([('device', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='module',
            unique_together=set([('device', 'parent', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='interfacetemplate',
            unique_together=set([('device_type', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='interface',
            unique_together=set([('device', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='devicetype',
            unique_together=set([('manufacturer', 'slug'), ('manufacturer', 'model')]),
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together=set([('rack', 'position', 'face')]),
        ),
        migrations.AlterUniqueTogether(
            name='consoleserverporttemplate',
            unique_together=set([('device_type', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='consoleserverport',
            unique_together=set([('device', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='consoleporttemplate',
            unique_together=set([('device_type', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='consoleport',
            unique_together=set([('device', 'name')]),
        ),
    ]
