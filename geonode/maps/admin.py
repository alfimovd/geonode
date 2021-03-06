# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from autocomplete_light.forms import modelform_factory

from geonode.maps.models import Map, MapLayer, MapSnapshot
from geonode.base.admin import MediaTranslationAdmin, ResourceBaseAdminForm
from geonode.base.admin import metadata_batch_edit
from django.contrib import admin


class MapLayerInline(admin.TabularInline):
    model = MapLayer


class MapAdminForm(ResourceBaseAdminForm):

    class Meta:
        model = Map
        fields = '__all__'


class MapAdmin(MediaTranslationAdmin):
    inlines = [MapLayerInline, ]
    list_display_links = ('title',)
    list_display = ('id', 'title', 'owner', 'is_published', 'featured',)
    list_filter = ('owner', 'category', 'featured', 'is_published',)
    search_fields = ('title', 'abstract', 'purpose',)
    form = MapAdminForm
    actions = [metadata_batch_edit]


class MapLayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'map', 'name')
    list_filter = ('map',)
    search_fields = ('map__title', 'name',)
    form = modelform_factory(MapLayer, fields='__all__')


admin.site.register(Map, MapAdmin)
admin.site.register(MapLayer, MapLayerAdmin)
admin.site.register(MapSnapshot)
