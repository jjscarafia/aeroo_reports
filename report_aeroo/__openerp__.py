# -*- encoding: utf-8 -*-
################################################################################
#                                                                       
# Copyright (C) 2009  Domsense s.r.l.
# @authors: Simone Orsi
#
# Copyright (c) 2009-2014 Alistek ( http://www.alistek.com ) All Rights Reserved.
#                    General contacts <info@alistek.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This module is GPLv3 or newer and incompatible
# with OpenERP SA "AGPL + Private Use License"!
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
################################################################################

{
    'name': 'Aeroo Reports',
    'version': '1.2.1',
    'category': 'Generic Modules/Aeroo Reporting',
    'description': """
Aeroo Reports for Odoo is a comprehensive and versatile reporting engine based
on Aeroo Library.

Report templates in the following formats:
================================================================================
* Open Document Format (ODF) - .odt, .ods;
* Other ASCII based formats, like HTML, CSV, etc.

Output formats:
================================================================================
* Open Document Format (ODF) - .odt, .ods;
* Other ASCII based formats, like HTML, CSV, etc. 
* using Aeroo DOCS - PDF, DOC, XLS, CSV.

Reporting engine features:
================================================================================
* Add reports from UI "on the fly";
* Install reports from module;
* Dynamic template load/unload;
* Extra Functions - set of functions for rapid template development;
* Use templates stored on filesystem, database or elsewhere;
* Same button - different templates;
* Powerful stylesheet system for ODF templates;
* Global or local stylesheets;
* Template preloading for performance concerns;
* User defined parsers;
* Report deactivation;
* Optional format fallback;
* Add/Remove print button wizards;
* Test report on particular object ID, directly from Report form;
* Translatable reports;
* Translation export;
* Number of copies;
* Universal Report wizard;
* Override report file extension (for direct printing, etc);
* Separate input/output format selections;

Input - Output format pairs:
================================================================================
* odt - odt/doc/pdf;
* ods - ods/xls/pdf/csv;
* html - html;

""",
    'author': 'Alistek & Simone Orsi (Domsense)',
    'website': 'http://www.alistek.com',
    'complexity': "easy",
    'depends': ['base'],
    'data': [
             "report_view.xml",
             "data/report_aeroo_data.xml", 
             "wizard/add_print_button_view.xml",
             "wizard/remove_print_button_view.xml",
             "installer.xml",
             "security/ir.model.access.csv"
             ],
    "license" : "GPL-3 or any later version",
    'installable': True,
    'active': False,
    'application': True,
    'auto_install': False,
}
