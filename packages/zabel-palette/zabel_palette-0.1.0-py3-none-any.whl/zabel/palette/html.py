# Copyright (c) 2019 Martin Lafaix (martin.lafaix@external.engie.com)
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0

"""HTML helpers.

A collection of functions returning HTML elements.

It is up to the callers of those functions to ensure they are called
with 'sanitized' arguments.  If not, this may expose users to unexpected
behaviors.

If passed sanitized arguments, the functions will return safe HTML
elements.

It uses 3 translatable texts:

- Cancel
- Legend
- Filter...
"""

__all__ = [
    'make_block',
    'make_js_button',
    'make_action',
    'make_table',
    'make_element',
    'make_warning',
    'make_doughnut',
    'make_barchart',
    'make_linechart',
    'make_dialog',
    'make_select',
    'make_venn5',
]


from functools import reduce
from itertools import chain, combinations

from .i18n import gettext


########################################################################
# Constants

## Doughnuts

DOUGHNUT_COLORS = [
    '#17255f',
    '#00aaff',
    '#00817d',
    '#e71b7b',
    '#fbba00',
    '#bad903',
    '#f26b33',
    '#6d3e91',
    '#009640',
]

DOUGHNUT_POINT_TMPL = '{{value: {v}, backgroundColor:"{c}", label: "{l}"}}'

DOUGHNUT_TMPL = '''<div class="doughnut">
       <a href="{full}"><canvas id="{id}" height="200px" width="200px"></canvas></a>
       </div>
       <script>
       var ctx = document.getElementById("{id}").getContext("2d"); var myLineChart = new Chart(ctx, {{
            type: 'doughnut',
            data: {data},
            options: {{
                plugins: {{
                    legend: {{display: {legend}}},
                    title: {{
                        display: true,
                        align: 'start',
                        color: '#17365d',
                        font: {{
                            weight: 'normal',
                            lineHeight: 1.4
                        }},
                        padding: 0,
                        text: '{title}'
                    }},
                    subtitle: {{
                        display: true,
                        align: 'start',
                        color: '#7f7f7f',
                        font: {{
                            size: 9
                        }},
                        text: '{subtitle}'
                    }}
                }}
            }}
        }});
       </script>'''


## Barcharts&Linecharts

CHART_DATASET_COLORS = [
    '#17255f',
    '#00aaff',
    '#00817d',
    '#e71b7b',
    '#fbba00',
    '#bad903',
    '#f26b33',
    '#6d3e91',
    '#009640',
]

DATASET_TMPL = '''{{label: "{title}", backgroundColor: "{c}", borderColor: "{c}", pointBackgroundColor: "rgba(220,220,220,1)", pointBorderColor: "#fff", pointHoverBackgroundColor: "#fff", pointHoverBorderColor: "rgba(220,220,220,1)", fill: true, data: {data}}}'''

BARCHART_TMPL = '''<div style="width: 700px; height: 250px"><canvas id="{id}"></canvas></div>
       <script>
       var data = {{labels: {xaxis}, datasets: [{datasets}]}};
       var ctx = document.getElementById("{id}").getContext("2d"); var myLineChart = new Chart(ctx, {{
           type: 'bar',
           data: data,
           options: {{
               maintainAspectRatio: false,
               plugins: {{
                    legend: {{display: {legend}}},
                }},
                scales: {{
                    x: {{
                        stacked: {stacked}
                    }},
                    y: {{
                        stacked: {stacked}
                    }}
                }}
           }}
       }});
       </script>'''

LINECHART_TMPL = '''<div style="width: 700px; height: 250px"><canvas id="{id}"></canvas></div>
       <script>
       var data = {{labels: {xaxis}, datasets: [{datasets}]}};
       var ctx = document.getElementById("{id}").getContext("2d"); var myLineChart = new Chart(ctx, {{
           type: 'line',
           data: data,
           options: {{
               maintainAspectRatio: false,
               plugins: {{
                    legend: {{display: {legend}}},
                }}
           }}
       }});
       </script>'''


## Venn diagrams

VENN_COLORS = [
    '#fbba00',  #'#ffc300',  # orange
    '#00aaff',  # "00aaff',  # cyan
    '#17255f',  #'#005faa',  # blue
    '#e71b7b',  # e62d87',  # pink
    '#009640',  #'#69af23',  # green
]

VENN_TMPL = '''<!-- Created with Inkscape (http://www.inkscape.org/) -->
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   id="svg2"
   width="350"
   height="340"
   version="1.0">
  <metadata
     id="metadata7">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <path
     style="line-height:100%;text-align:center;writing-mode:lr-tb;text-anchor:middle;fill:{{c5}};fill-opacity:0.48618786;fill-rule:evenodd;stroke:{{c5}};stroke-width:1.06666672px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
     d="m 198.09787,191.27615 c -3.0105,0.82629 -6.01401,1.86506 -8.71385,3.43246 -2.15522,1.25122 -4.27637,2.56306 -6.46566,3.75367 -2.60016,1.41406 -5.34726,2.8553 -7.74159,4.28422 -2.42785,1.4489 -4.68988,3.16434 -7.11769,4.61334 l -7.29187,4.35206 c -2.16404,1.29159 -4.31735,2.60383 -6.52727,3.81525 -1.94656,1.06704 -3.92833,2.07185 -5.93683,3.01717 -2.41392,1.13614 -4.8065,2.34548 -7.32534,3.22484 -2.67495,0.93387 -5.44331,1.5905 -8.2105,2.19893 -2.43977,0.53643 -4.90697,0.9794 -7.39226,1.23166 l -7.79426,0.79116 -5.76169,0.13885 -9.89282,-0.37964 c -3.553175,-0.13635 -7.229345,-0.99448 -10.638217,-2.00603 -3.517017,-1.04365 -6.784497,-2.82104 -10.027577,-4.53599 -3.853028,-2.03749 -7.722834,-4.11109 -11.22675,-6.70333 L 58.410881,203.21282 48.277899,195.1746 c 0,0 -7.016234,-4.98772 -10.37503,-7.67561 -2.936881,-2.35025 -5.965083,-4.6349 -8.536833,-7.37991 -2.515367,-2.68483 -5.560212,-5.44119 -7.791449,-8.36642 -1.461049,-1.91548 -2.586682,-4.03292 -3.708907,-6.16466 -1.326043,-2.51891 -3.197209,-5.63691 -3.940864,-8.38469 -0.918958,-3.39551 -1.339936,-3.17692 -2.251616,-10.13582 -0.760341,-5.80372 -0.576815,-9.31943 0.363169,-17.46022 0.782507,-6.77696 4.295525,-13.53822 7.034363,-19.78472 2.950753,-6.72982 4.428712,-8.81829 4.428712,-8.81829 l 5.294636,-8.155 c 2.743537,-4.225703 5.753011,-8.301082 8.91011,-12.22744 2.407331,-2.993903 5.097576,-5.783555 7.781943,-8.531805 3.229611,-3.306468 6.777296,-6.294602 10.345349,-9.232649 2.758025,-2.271045 5.742319,-4.252432 8.613478,-6.378647 2.871159,-2.126216 4.69707,-3.253041 10.659333,-6.088009 5.22777,-2.485727 7.072294,-2.937592 10.254699,-3.731533 4.939644,-1.232334 6.599293,-1.893622 13.055239,-1.875012 3.235939,0.0093 6.421649,0.523746 8.413269,0.863057 1.9916,0.33931 3.43751,0.761917 6.29872,1.660001 3.71181,1.165075 5.24612,2.134136 8.66297,3.434931 5.02478,1.912931 9.86997,4.377594 14.54058,7.052672 4.74779,2.719279 7.42445,4.313944 10.02665,6.717536 2.60219,2.403591 5.37521,4.63452 7.80659,7.210774 1.65351,1.752034 3.06035,3.73073 4.40568,5.729173 1.64326,2.440966 3.06863,4.957529 4.7197,7.39321 1.93852,2.859736 4.03935,6.018333 6.47079,8.472731 3.45161,3.48421 6.23052,7.7987 10.35484,10.45263 3.51997,2.26505 7.95911,3.11781 11.93867,4.41542 3.97957,1.29763 7.88311,2.3344 11.93868,3.37029 5.30723,1.35558 10.54943,2.38426 15.84293,3.7925 l 7.82679,2.08215 c 4.1573,1.10597 8.55349,1.97399 12.52911,3.61736 3.68253,1.52222 8.35409,3.26852 11.77738,5.30792 2.29201,1.36545 4.37073,2.41561 6.66276,3.78106 2.85707,1.70207 5.32969,3.8602 7.88939,5.98337 2.10031,1.74212 3.93842,3.34632 6.32984,6.74015 2.9095,4.12909 3.50876,8.87207 4.95482,13.71185 0.93783,3.13877 0.59142,6.62763 0.84386,9.89377 0.25499,3.29931 0.19331,6.66646 -0.37052,9.92722 -0.41014,2.37194 -0.60002,4.79268 -1.23041,7.11581 -0.6309,2.32501 -1.88035,4.87469 -3.32073,7.0287 -1.44562,2.16186 -3.23606,4.08223 -5.24602,5.77497 -1.6515,1.13164 -3.451,1.85778 -5.34643,2.21909 -2.79627,0.53303 -5.69244,0.60173 -8.53867,0.55416 -3.15887,-0.27645 -6.69472,-0.86648 -9.46166,-2.05744 -2.52183,-1.04244 -5.30604,-2.1788 -7.55056,-3.33136 -2.6644,-1.3682 -5.37927,-2.5399 -8.31525,-3.13239 -2.79038,-0.56311 -5.45898,-1.09998 -8.29235,-1.37434 -2.94601,-0.28527 -6.04301,-0.48191 -8.99272,-0.23783 -1.86969,0.15472 -3.7027,0.1842 -5.55406,0.46108 -2.777,0.4153 -5.62326,1.11855 -8.331,1.86176 z"
     id="p5" />
  <path
     style="line-height:100%;text-align:center;writing-mode:lr-tb;text-anchor:middle;fill:{{c2}};fill-opacity:0.49019608;fill-rule:evenodd;stroke:{{c2}};stroke-width:1.06666672;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
     d="m 158.75303,209.15343 -6.37955,-6.82953 -5.32179,-5.16181 -6.41195,-6.1425 -6.70559,-5.19417 -6.7056,-5.19418 -5.75725,-4.90054 -4.80894,-4.60687 -5.46363,-5.84884 -5.86673,-6.79716 c -1.68872,-1.95653 -2.25354,-2.69443 -3.67645,-4.89368 -1.40395,-2.16995 -2.615723,-3.80861 -3.699056,-6.15513 -0.808793,-1.75185 -1.933853,-5.28642 -2.247656,-7.19028 -0.530033,-3.21573 -0.82957,-6.86817 -1.498785,-10.05785 -0.734977,-3.50313 -0.54738,-7.43766 -0.95673,-10.99357 -0.43177,-3.75067 0.05074,-7.57146 0.559418,-11.31246 0.579634,-4.26287 1.796654,-8.414523 2.694982,-12.621784 1.036482,-4.854301 2.434944,-10.317235 4.056397,-15.008655 l 4.06905,-11.773196 4.16588,-12.241044 c 1.17757,-3.460182 3.25997,-7.926035 5.22364,-11.008818 1.87988,-2.95126 4.09441,-5.911312 5.98802,-8.853779 1.30373,-2.025841 3.18997,-4.726001 4.7361,-6.573489 2.23051,-2.665273 4.68604,-5.60968 6.62295,-7.695765 2.00442,-2.158806 5.83298,-4.695156 7.9423,-5.70518 2.5746,-1.232807 9.94088,-3.41195 13.84877,-3.817186 6.82071,-0.707288 15.15814,-0.569176 22.35075,0.260504 7.30141,0.842229 9.6664,1.405017 12.44301,2.17359 2.92385,0.809329 6.12262,1.758363 9.00289,2.675233 4.5966,1.463222 8.00156,2.644499 12.47067,4.244106 3.92175,1.403696 7.94294,2.881977 11.503,4.641137 4.03516,1.99393 8.35045,3.88282 12.19867,6.217224 3.16323,1.918865 5.76305,3.534958 8.79903,5.649393 3.28111,2.285159 6.29655,4.992454 8.96325,7.971776 2.51634,2.811336 4.52698,6.052482 6.4793,9.281109 2.17941,3.604153 3.73786,7.462887 4.84683,11.526124 1.21356,4.446475 3.0442,8.675746 3.3628,13.273828 0.23507,3.392443 0.85391,6.780006 0.70519,10.177328 -0.2356,5.381746 -0.79802,10.771574 -1.85349,16.054064 -0.8429,4.2185 -1.67403,8.74133 -2.94652,12.85073 -0.97885,3.16105 -2.24829,5.97911 -3.58977,9.00416 -0.97661,2.20226 -2.71342,4.22644 -4.16994,6.00736 l -5.70703,6.97807 -6.21695,8.0361 c -3.06414,3.96075 -4.88523,8.83425 -6.30143,13.63746 -1.20793,4.09681 -1.56413,8.45844 -1.47248,12.72863 0.0897,4.17989 1.39884,8.24449 2.01136,12.38024 0.8025,5.4185 1.75878,8.19811 2.05923,13.66748 l 0.59257,10.78673 c 0.23499,4.2778 0.73459,8.58141 0.3468,12.84808 -0.36068,3.96839 -0.91048,8.11705 -1.70456,12.02187 -0.53167,2.61441 -0.898,5.95688 -1.4009,8.57697 -0.62689,3.26604 -1.70075,5.61431 -2.85917,8.73168 -0.95053,2.55789 -2.39639,4.99281 -4.24585,6.99924 -3.42349,3.71406 -7.31364,7.01529 -11.40404,9.97892 -2.65278,1.92203 -5.6944,3.26547 -8.6938,4.58266 -3.02986,1.33057 -6.09866,2.7168 -9.34846,3.34067 -2.3659,0.45419 -4.46865,0.93921 -6.87716,0.88623 -2.40851,-0.053 -5.37282,-0.27931 -7.74811,-0.68151 -2.61015,-0.44199 -5.12434,-1.54014 -7.41235,-2.8718 -1.66766,-0.9706 -4.2286,-3.09323 -5.25419,-4.66162 -1.55793,-2.38248 -2.20502,-4.77335 -2.88133,-7.64366 -0.71998,-3.05566 -0.94542,-5.67023 -0.74451,-8.91439 0.16867,-2.72356 0.64942,-6.004 0.73628,-8.78972 0.0923,-2.95835 -0.18586,-6.93326 -0.58184,-9.99288 -0.36536,-2.8231 -0.58815,-4.10981 -1.26515,-6.87477 -0.70392,-2.87486 -1.17032,-5.1827 -2.01018,-8.02084 -0.53118,-1.795 -1.1327,-5.58279 -2.22673,-7.10175 z"
     id="p2" />
  <path
     style="line-height:100%;text-align:center;writing-mode:lr-tb;text-anchor:middle;fill:{{c3}};fill-opacity:0.48618788;fill-rule:evenodd;stroke:{{c3}};stroke-width:1.06666672px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
     d="m 128.31879,174.09915 6.00888,-7.59356 4.45887,-7.12339 3.88388,-7.85486 3.58791,-8.72583 c 0.99532,-2.42065 2.3794,-4.66672 3.4137,-7.07098 0.95323,-2.21582 2.2522,-4.36295 3.15244,-6.60081 0.73742,-1.83313 1.79103,-3.90618 2.62984,-5.69518 1.04267,-2.22378 2.1828,-4.22636 3.2742,-6.42664 1.26494,-2.55015 3.04017,-5.80886 4.52824,-8.16855 1.37861,-2.18615 3.01244,-4.55076 4.56292,-6.61856 1.56624,-2.08882 2.9991,-3.661372 4.92017,-5.390328 1.43422,-1.290797 3.19433,-3.029821 4.92016,-4.154029 2.73086,-1.778876 4.95346,-2.910779 7.80245,-4.493553 3.12895,-1.738306 5.95929,-2.345392 9.37018,-3.430678 4.11149,-1.308203 8.65623,-1.987563 12.90565,-2.734671 4.32381,-0.760189 8.57979,-0.80805 12.90567,-1.288703 4.6162,-0.512911 9.39777,-0.384847 13.89842,-0.193951 l 11.78976,0.500067 13.02883,0.739036 c 3.64921,0.206994 7.15695,0.415477 10.79701,0.74639 3.64006,0.330914 7.43801,0.638201 11.04335,1.239092 2.37632,0.396055 4.74209,1.019883 6.94921,1.985494 3.12132,1.365578 6.24538,2.872035 8.93469,4.963712 3.32464,2.585827 6.4574,5.528409 8.93469,8.934688 2.87375,3.951404 4.95136,8.446914 6.94922,12.905674 2.31631,5.16952 4.4574,10.45261 5.96381,15.91336 1.15477,4.18607 1.60285,8.55004 1.97813,12.87622 0.28599,3.29677 0.48868,6.62074 0.61586,9.92744 0.20389,5.30104 0.046,10.58926 0.37689,15.88389 0.33091,5.29464 0.21453,7.94776 0,11.91293 -0.25162,4.65073 -0.28961,9.39557 -1.50752,13.89105 -0.94882,3.50224 -1.72498,7.61274 -3.21723,10.92018 -1.64438,3.64467 -4.12655,6.5132 -6.19543,9.9348 -1.95224,3.22868 -6.94921,8.93469 -6.94921,8.93469 0,0 -6.98084,6.83894 -9.67374,8.68835 -3.81606,2.62076 -7.67051,4.51158 -11.67393,6.44179 -3.04436,1.46781 -6.16051,2.86592 -9.42739,3.732 -5.20702,1.38042 -10.52559,2.42392 -15.88389,2.97823 -4.27906,0.44265 -8.5422,0.30793 -12.84409,0.30793 -3.30914,0 -7.17992,-0.38516 -9.49633,-1.04697 -2.3164,-0.66184 -4.95876,-1.33712 -7.19555,-2.23184 -2.7481,-1.09925 -5.42976,-1.91282 -8.1883,-2.98559 -3.21994,-1.25219 -6.53968,-2.30068 -9.92743,-2.97823 -4.9104,-0.98208 -9.8972,-2.3554 -14.89116,-1.98548 -4.17434,0.30921 -8.43464,1.66193 -12.40561,2.98559 -3.97098,1.32365 -7.62716,3.18626 -11.42024,4.95636 0,0 -9.92743,4.6328 -14.89115,6.9492 -2.58831,1.20789 -5.21294,2.37409 -7.94196,3.21721 -3.98807,1.23209 -8.06492,2.18104 -12.15926,2.99296 -3.85637,0.76473 -7.77252,1.19071 -11.66658,1.73177 -2.64253,0.36717 -5.28728,0.72728 -7.94194,0.99275 -3.30914,0.33091 -6.58493,0.73149 -9.31158,0.62322 -2.7089,-0.10756 -6.00699,-0.22503 -9.69006,-1.35469 -4.829149,-1.48116 -8.900892,-2.85701 -13.341146,-5.67742 -3.043658,-1.93332 -5.979528,-4.34301 -7.907264,-6.86212 -2.011036,-2.62795 -4.312108,-6.67695 -5.433869,-9.68388 -0.84205,-2.25714 -1.672051,-4.98117 -2.159687,-7.47178 -0.462892,-2.3642 -1.144511,-4.99672 -1.027424,-7.55888 0.120853,-2.64455 0.115438,-5.97844 1.219347,-8.37742 0.811016,-1.76249 2.472235,-4.61878 3.936288,-5.92179 1.793821,-1.59651 4.156581,-2.79778 5.90404,-3.39599 2.920204,-0.99966 5.92915,-2.32181 8.847592,-3.3266 2.580156,-0.88832 5.502283,-1.73894 8.029049,-2.76935 2.676349,-1.09141 5.396564,-2.08089 8.029044,-3.27422 2.59644,-1.17699 5.16389,-2.42931 7.64598,-3.83146 2.48775,-1.40534 4.97302,-2.84826 7.24517,-4.58065 1.48862,-1.13497 3.9146,-2.61193 5.10323,-4.05807 z"
     id="p3" />
  <path
     style="line-height:100%;text-align:center;writing-mode:lr-tb;text-anchor:middle;fill:{{c1}};fill-opacity:0.48618786;fill-rule:evenodd;stroke:{{c1}};stroke-width:1.06666672px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
     d="m 150.90052,142.40889 c 2.95343,1.0115 6.04955,1.58882 9.13447,2.06754 2.49036,0.38645 4.86096,0.78982 7.36838,1.04297 2.94482,0.29731 6.03018,0.38179 8.98133,0.60771 2.81909,0.21581 5.65321,0.12873 8.47981,0.19308 2.8266,0.0643 5.65528,0.0673 8.47982,0.19307 2.51768,0.11212 5.03411,0.27784 7.54258,0.52041 2.20954,0.21367 4.41313,0.4986 6.60535,0.84773 2.63472,0.4196 7.43241,1.39512 7.43241,1.39512 l 8.72182,2.37026 c 2.54563,0.69181 5.26183,1.83603 7.69526,2.85449 2.49418,1.04389 4.63368,2.10851 6.99871,3.41895 2.25609,1.25009 4.27312,2.89128 6.36444,4.40094 2.66899,1.92667 5.4388,3.73661 7.9142,5.90639 2.51169,2.2016 4.93756,4.54198 7.00159,7.16788 2.37147,3.01703 4.32213,6.35094 6.23807,9.67591 1.95701,3.39621 4.23193,6.71123 5.36666,10.4631 1.51004,4.99276 3.09947,9.12282 4.6355,14.10763 1.3283,4.31061 2.76481,8.58935 3.98487,12.93185 1.17904,4.19645 2.14006,8.4511 3.21008,12.67666 1.07003,4.22556 1.29642,7.00874 1.7396,10.63684 0.45518,3.72628 0.35511,8.72708 0.4194,12.46164 0.0415,2.40873 0.19639,4.08256 -0.0758,6.47621 -0.32175,2.82838 -0.9702,6.98554 -1.90213,9.6753 -1.15163,3.32382 -2.45611,6.84702 -3.94199,10.03547 -2.47297,5.30654 -4.80293,9.45261 -8.74877,13.77757 -4.59792,5.03969 -11.16687,7.8796 -17.10793,11.23267 -2.60961,1.47285 -5.07072,2.61788 -8.10772,3.88317 -3.05465,1.27264 -6.1647,2.56049 -9.1981,3.88294 -4.85028,2.11453 -9.83303,3.81902 -14.84252,5.56477 -3.73434,1.30138 -7.60053,2.24486 -11.49309,2.94254 -4.37386,0.78395 -8.65229,1.47463 -13.07274,1.9272 -3.65041,0.37374 -7.47028,0.44905 -11.13834,0.55161 -3.98217,0.11135 -8.02187,0.33911 -11.94615,-0.34651 -3.71671,-0.64935 -7.23759,-2.17798 -10.72637,-3.61466 -3.89456,-1.60377 -7.85949,-3.17851 -11.38097,-5.48912 -3.55928,-2.33541 -7.09477,-4.94837 -9.68044,-8.33023 l -6.89305,-9.01553 c 0,0 -5.80973,-9.11421 -8.04891,-14.01368 -1.78817,-3.91263 -3.41856,-8.04542 -4.86492,-12.09688 -1.11074,-3.11129 -1.88366,-6.46455 -2.26416,-9.74617 -0.29634,-2.55575 -0.0512,-5.19995 0.0547,-7.62522 0.12916,-2.95698 0.1364,-5.15314 0.25933,-8.11038 0.14349,-3.45187 -0.30772,-6.90283 -0.46159,-10.35426 -0.22301,-5.00268 -1.03959,-10.12035 -3.03542,-14.71308 -1.66828,-3.83895 -4.0808,-7.44672 -6.89298,-10.5471 l -8.46068,-9.32776 -11.47051,-11.76716 c -2.010889,-2.06289 -3.844398,-4.5129 -5.538222,-6.84317 -2.604126,-3.58261 -5.083701,-6.9992 -7.307625,-10.82945 -1.836326,-3.16268 -3.485917,-6.43154 -5.12642,-9.70009 L 68.0713,158.39628 c -1.491803,-2.97228 -3.115609,-5.588 -4.036293,-8.78366 -0.75545,-2.62213 -0.914092,-5.42898 -0.744171,-8.15248 0.314537,-5.0414 1.593748,-10.02809 3.242592,-14.80259 1.069337,-3.09645 2.640619,-6.00957 4.269312,-8.8519 1.645225,-2.87118 3.656516,-5.70108 5.969348,-8.06777 1.683776,-1.72298 3.501825,-3.38685 5.470481,-4.77543 1.968646,-1.38858 4.974399,-3.90253 7.473674,-4.7754 2.499275,-0.872878 3.298546,-1.284942 5.930092,-1.573472 1.918058,-0.210301 3.930168,0.336838 5.668135,1.175072 2.56399,1.23663 4.76048,3.21192 6.62903,5.35943 l 5.67053,7.27889 5.36402,6.40769 6.36753,6.10144 6.54194,5.18524 6.62882,5.31756 4.79694,3.31058 c 2.31095,1.59489 4.93086,2.74962 7.58726,3.65941 z"
     id="p1" />
  <path
     style="line-height:100%;text-align:center;writing-mode:lr-tb;text-anchor:middle;fill:{{c4}};fill-opacity:0.48618786;fill-rule:evenodd;stroke:{{c4}};stroke-width:1.06666672px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
     d="m 195.95744,153.4821 0.27025,9.43989 1.54525,7.40091 1.30129,8.7835 2.11457,8.2142 2.11457,8.21419 1.54525,7.40093 0.97596,6.58762 0.73196,7.97022 -0.0813,8.53951 -1.11869,7.61289 c -0.37576,2.55707 -0.98278,5.07752 -1.56512,7.5956 -0.43474,1.87993 -0.74276,3.67682 -1.66176,5.37346 -1.55227,2.86573 -2.83219,5.79478 -4.2585,8.72524 -1.56648,3.21842 -3.55265,6.4928 -5.38438,9.56799 -1.93082,3.24153 -4.54504,6.05979 -7.23824,8.70218 -3.07979,3.02169 -6.46877,5.73993 -10.00342,8.2142 l -12.19928,8.53956 -10.70656,7.02312 c 0,0 -7.2887,4.39941 -10.9211,6.70416 -3.08625,1.95822 -6.19659,3.91781 -9.51546,5.44905 -3.42595,1.58065 -6.31122,2.91814 -9.87018,4.17087 -2.27243,0.79988 -3.91815,1.29174 -6.13302,1.49194 -4.25071,0.38422 -7.18025,0.60422 -10.02197,0.43645 -3.51155,-0.20733 -7.280726,-0.31208 -10.752689,-0.87728 -5.778416,-0.94068 -10.533641,-2.51004 -15.766845,-5.13465 -6.09803,-3.05834 -11.745705,-7.47829 -16.584731,-12.28695 -2.125546,-2.11221 -3.628509,-3.70236 -6.106829,-6.35525 -2.47832,-2.65289 -4.76668,-5.40741 -7.003856,-8.2666 -3.098717,-3.96027 -6.609516,-7.86442 -9.452377,-12.01217 -2.842861,-4.14775 -3.930614,-6.74681 -5.907842,-10.19053 -2.280623,-3.97214 -4.148,-8.18904 -5.749021,-12.48041 -1.268357,-3.39969 -2.195613,-6.92399 -3.03451,-10.45428 -0.924405,-3.89013 -1.493151,-7.80313 -1.760422,-11.79265 -0.252203,-3.76457 -0.289765,-7.55554 0.133777,-11.3047 0.472804,-4.18524 0.578531,-7.48859 2.195872,-12.4433 1.430256,-4.38158 4.258632,-8.61735 6.855235,-12.42544 l 6.563376,-9.62563 c 3.034781,-4.45071 6.160306,-7.25727 10.172421,-10.85193 3.15474,-2.8265 6.804791,-5.42388 10.22433,-7.92352 2.671493,-1.95284 4.91779,-3.56796 8.045767,-4.64787 2.277202,-0.78617 4.660268,-1.4604 7.005799,-2.01014 2.881701,-0.67541 4.642963,-1.17635 7.457684,-2.09164 l 10.811736,-3.51575 c 0,0 9.241145,-4.44046 13.071425,-7.62522 3.21856,-2.67612 8.27773,-8.4938 8.27773,-8.4938 l 7.48221,-10.08477 8.56258,-13.79708 5.0193,-6.61648 8.56774,-9.852902 7.53531,-8.690071 c 1.74782,-2.01567 3.93367,-4.21543 5.93699,-5.977396 2.4972,-2.196345 4.73748,-4.143563 7.56355,-5.896641 2.31887,-1.438447 5.04083,-2.998686 7.73197,-3.450417 4.9815,-0.836191 13.17613,-1.156624 15.91103,-0.807557 2.57722,0.328941 5.3698,0.782834 7.5007,1.53369 3.10755,1.094991 7.15639,2.631458 10.1309,4.048533 2.1749,1.036134 4.96048,2.426601 6.83105,3.944737 1.87056,1.51813 3.37177,3.041977 5.00201,4.815678 1.79146,1.949093 3.04024,3.354923 4.03183,5.809513 0.72275,1.789086 0.65488,4.658037 0.31956,6.558234 -0.49469,2.803309 -0.88099,5.461408 -2.23679,7.964419 -1.4952,2.7604 -3.65232,5.11077 -5.61167,7.56359 -1.70311,2.13206 -4.06801,3.78159 -5.36768,6.181 l -4.22907,7.80758 c -1.3558,2.50302 -2.1657,5.23416 -3.32553,7.83378 -1.20594,2.70298 -2.67405,5.26804 -3.75005,8.02532 -0.68052,1.74386 -1.12966,3.64337 -1.45496,5.48682 -0.48798,2.76534 -0.8475,5.44555 -0.76715,8.25245 z"
     id="p4" />
  <text {text} x="205.24002" y="302.04782" id="d1">{{d1}}</text>
  <text {text} x="183.78929" y="47.905422" id="d2">{{d2}}</text>
  <text {text} x="291.6087"  y="134.27408" id="d3">{{d3}}</text>
  <text {text} x="73.205116" y="275.24371" id="d4">{{d4}}</text>
  <text {text} x="48.403004" y="110.06718" id="d5">{{d5}}</text>
  <text {text} x="211.04698" y="267.30176" id="d12">{{d12}}</text>
  <text {text} x="258.35965" y="235.53401" id="d13">{{d13}}</text>
  <text {text} x="148.16508" y="279.21469" id="d14">{{d14}}</text>
  <text {text} x="80.154297" y="140.92758" id="d15">{{d15}}</text>
  <text {text} x="240.82932" y="107.47002" id="d23">{{d23}}</text>
  <text {text} x="181.26469" y="83.644196" id="d24">{{d24}}</text>
  <text {text} x="118.87132" y="87.615128" id="d25">{{d25}}</text>
  <text {text} x="97.535126" y="245.46143" id="d34">{{d34}}</text>
  <text {text} x="257.85544" y="160.08545" id="d35">{{d35}}</text>
  <text {text} x="60.299454" y="191.85329" id="d45">{{d45}}</text>
  <text {text} x="222.95992" y="228.58479" id="d123">{{d123}}</text>
  <text {text} x="185.36053" y="252.41058" id="d124">{{d124}}</text>
  <text {text} x="107.3429"  y="128.31767" id="d125">{{d125}}</text>
  <text {text} x="144.19408" y="242.4832"  id="d134">{{d134}}</text>
  <text {text} x="249.15744" y="189.71989" id="d135">{{d135}}</text>
  <text {text} x="91.937698" y="175.96938" id="d145">{{d145}}</text>
  <text {text} x="201.24442" y="102.65416" id="d234">{{d234}}</text>
  <text {text} x="221.12392" y="141.2233"  id="d235">{{d235}}</text>
  <text {text} x="147.05269" y="110.44827" id="d245">{{d245}}</text>
  <text {text} x="88.959473" y="216.52402" id="d345">{{d345}}</text>
  <text {text} x="186.35327" y="217.66461" id="d1234">{{d1234}}</text>
  <text {text} x="215.552"   y="170.85782" id="d1235">{{d1235}}</text>
  <text {text} x="121.82508" y="152.89458" id="d1245">{{d1245}}</text>
  <text {text} x="126.88725" y="208.09598" id="d1345">{{d1345}}</text>
  <text {text} x="179.81323" y="129.45822" id="d2345">{{d2345}}</text>
  <text {text} x="163.92935" y="180.78522" id="d12345">{{d12345}}</text>
  <text {title} x="87.61026" y="395.75278" id="n1" transform="rotate(-23.05059)">{{n1}}</text>
  <text {title} x="202.69258" y="-63.788029" id="n2" transform="rotate(22.17734)">{{n2}}</text>
  <text {title} x="130.16261" y="-334.40262" id="n3" transform="rotate(93.182753)">{{n3}}</text>
  <text {title} x="228.65565" y="153.21391" id="n4" transform="rotate(51.24936)">{{n4}}</text>
  <text {title} x="-41.315285" y="75.302536" id="n5" transform="rotate(-46.212945)">{{n5}}</text>
</svg>
'''.format(
    text='xml:space="preserve" style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:12.80000019px;line-height:100%;font-family:Arial;text-align:center;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.06666672"',
    title='xml:space="preserve" style="font-style:normal;font-weight:normal;font-size:10.66666698px;line-height:125%;font-family:Arial;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.06666672"',
)


## Requests

REQUEST_TMPL = '<p class="mailto">+&nbsp;{request}</p>'


## Buttons

ACTIVE_BUTTON_TMPL = (
    '<input type="button" value="{label}" onclick="{onclick}"/> '
)
INACTIVE_BUTTON_TMPL = (
    '<input type="button" value="{label}" disabled="disabled"/> '
)
ACTION_BUTTON_TMPL = '<input class="ok" type="button" onclick="javascript:do_form(\'{id}form\');" value="{label}" />'


## Actions

ACTION_TMPL = '<a href="javascript:show_newapp(\'{action}\');">{label}</a>'


## Tables

SEARCH_BUTTON_TMPL = '<input class="search" placeholder="{filter}" />'

SEARCH_SCRIPT_TMPL = '''<script language="JavaScript">
       var options = {{
           valueNames: {options}
       }};
       var userList = new List('table_{t}', options);
       </script>'''

ELEMENTS_TABLE_TMPL = '''<div id="table_{t}"{style}>
       {search}
       <table class="elements">
       <tr>
           {headers}
       </tr>
       <tbody class="list">
           {rows}
       </tbody>
       </table>
       </div>
       {extra}'''


## Elements

ELEMENT_TMPL = '<span class="{status}"{title}>{text}</span>'
LINK_ELEMENT_TMPL = '<a href="{target}" title="{title}">{element}</a>'


## Blocks

BEGIN_BLOCK_TMPL = '''<div class="block">
           <h2>%s</h2>
           <p class="sub-header">%s</p>'''

END_BLOCK_TMPL = '</div>'

BLOCK_LEGEND_TMPL = '''<h3>{legend}</h3>
       <div class="legend">
           %s
       </div>'''


## Misc.

DIALOG_TMPL = '''<div id="{{id}}" class="dialog">
       <h2>{{title}}</h2>
       <form id="{{id}}form" name="{{id}}form" action="?a={{id}}" method="post">
       <table>
       <div class="detailsBody">
       {{body}}
       </div>
       <tr>
           <td colspan="2">
               <input class="cancel" type="button"
                      onclick="javascript:hide_newapp('{{id}}');"
                      value="{cancel}" />
               {{action_button}}
           </td>
       </tr>
       </table>
       </form>
       </div>'''

WARNING_TMPL = '''<div class="info">
           <p>{text}</p>
       </div>'''


# Le format des requêtes utilisateur
#
# De nouveaux types d'objet peuvent être ajoutés, et les valeurs
# associées changées à loisir.
#
# Si les éléments référencés par ces valeurs ne sont pas spécifiés dans
# les dictionnaires 'data' des requêtes de type correspondant, la
# requête ne sera pas générée par l'application (une entrée REQUETE
# INVALIDE sera émise à la place, n'incluant aucun lien)

REQUEST_OBJECT = {
    'mailto': '<a href="{mailto}?Subject={subject}&amp;body={body}">{title}</a>',
    'link': '<a href="{target}">{title}</a>',
}


########################################################################
# Functions


def make_block(title, subtitle, items, requests=[], legend=None, extra=None):
    """Return HTML-ready block section.

    A block section is made of a title, a sub-title, a collection of
    items, an optional collection of requests with optional extras, and
    an optional legend.

    If the collection of items is empty, the legend is ignored.
    """
    block = BEGIN_BLOCK_TMPL % (title, subtitle)

    for item in items:
        block += item

    for request in requests:
        block += _make_request(request, extra)

    block += END_BLOCK_TMPL

    if items and legend:
        block += BLOCK_LEGEND_TMPL.format(legend=gettext('Legend')) % legend

    return block


def make_js_button(label, onclick=None):
    """Return HTML-ready representation for button with onclick action.

    If no `onclick` action provided, the button is disabled.

    It is up to the caller to sanitize the label, if needed.
    """
    if onclick is None:
        return INACTIVE_BUTTON_TMPL.format(label=label)
    else:
        return ACTIVE_BUTTON_TMPL.format(label=label, onclick=onclick)


def make_action(label, action):
    """Return HTML-ready representation for action.

    It is up to the caller to sanitize the label, if needed.
    """
    return ACTION_TMPL.format(label=label, action=action)


def _make_request(r, extra=None):
    """Return HTML-ready representation for request r.

    `extra` is an optional dictionary used to format the request text.
    If not specified, no format operation occurs. If specified, it is
    passed as an argument to the format() function.

    If the `format()` call fails, the `'unformatted'` value is returned.

    Request types are defined in REQUEST_OBJECT.

    It is up to the caller to sanitize the request, if needed.
    """
    rq = REQUEST_OBJECT[r['type']].format(**r['data'])
    if extra is not None:
        try:
            rq = rq.format(**extra)
        except:
            # logging.debug('make_request', 'extra missing keys for', rq)
            pass

    return REQUEST_TMPL.format(request=rq)


_table_cpt = 0  # used to generate unique IDs for tables


def make_table(
    source, cols, large=True, searchable=None, width=None, sortable=False
):
    """Return HTML-ready tabular representation for source.

    - `source`: a collection of rows
    - `cols`: [(index, header, width, fn[, key]), ...]
    - `large`: large table or scrollable view on table
    - `searchable`: search specified cols? (only for large tables)
    - `width`: table width, in em (full available width if unspecified)

    - `index`: nth item in row (if None, full row passed to function)
    - `header`: column header (may contain html elements)
    - `width`: column width (if negative, right-align content)
    - `fn`: formatting function (one parameter, the value to format)
    - `key`: (optional) column name (for searchable tables)

    It is up to the caller to sanitize the headers, if needed. The
    cells values are expected to be sanitized by `fn`, if needed.
    """
    global _table_cpt

    _table_cpt += 1
    style = '' if large else 'overflow-y:auto; max-height:200px;'
    if width is not None:
        style += 'width: %dem;' % width
    if style != '':
        style = ' style="%s"' % style

    if large and searchable is not None:
        search = SEARCH_BUTTON_TMPL.format(filter=gettext('Filter...'))
        script = SEARCH_SCRIPT_TMPL.format(t=_table_cpt, options=searchable)
    else:
        search = script = ''

    right_aligned_header = ' class="number"'
    headers = [
        '<th width="{width}%"{cls}>{header}{sorting_button}</th>'.format(
            header=c[1],
            width=abs(int(c[2])),
            cls=right_aligned_header if c[2] < 0 else '',
            sorting_button=f'<button class="sort" data-sort={c[4]}></button>'
            if sortable
            else '',
        )
        for c in cols
    ]

    right_aligned_data = ' style="text-align: right"'
    rows = [
        '<tr class="rowfile">%s</tr>'
        % ''.join(
            '<td{cls}{style}>{cell}</td>'.format(
                cls=' class="{n}"'.format(n=c[4]) if len(c) > 4 else '',
                cell=c[3](r if c[0] is None else r[c[0]]),
                style=right_aligned_data if c[2] < 0 else '',
            )
            for c in cols
        )
        for r in source
    ]

    return ELEMENTS_TABLE_TMPL.format(
        t=_table_cpt,
        style=style,
        search=search,
        extra=script,
        headers='\n'.join(headers),
        rows='\n'.join(rows),
    )


def make_element(
    title, status, primary, secondary=None, extra=None, target=None
):
    """Return HTML-ready representation for element.

    - `title` is the required title displayed as a bubble when hovering
        element.
    - `status` is the element status (not displayed, but used as a class
        to style the element).
    - `primary` is the primary text of the element.
    - `secondary` is the optional secondary text of the element.
    - `extra` is the optional item displayed after primary but before
        secondary.
    - `target` is the optional link target.

    It is up to the caller to sanitize the parameters, if needed.
    """
    if target is None:
        text = primary
        if extra is not None:
            text += '&nbsp;' + extra
        if secondary is not None:
            if extra is None:
                text += '&nbsp;'
            text += '<span class="server">' + secondary + '</span>'

        return ELEMENT_TMPL.format(
            status=status,
            text=text,
            title='' if title is None else ' title="%s"' % title,
        )

    return LINK_ELEMENT_TMPL.format(
        target=target,
        title=title,
        element=make_element(None, status, primary, secondary, extra),
    )


def make_warning(t, **extra):
    """Return HTML-ready representation for warning t.

    Substitutions are performed if extra keyword args are given.

    It is up to the caller to sanitize the parameters, if needed.
    """
    return WARNING_TMPL.format(text=t.format(**extra))


_doughnut_cpt = 0  # used to generate unique IDs for canvas


def make_doughnut(
    title, subtitle, counts, labels, link, colors=None, legend: bool = False
):
    """Return HTML-ready representation for doughnut.

    - `title` is doughnut's title.
    - `subtitle` is doughnut's subtitle.
    - `counts` is a dict with numerically-valued keys which must be
        keys in `labels`.
    - `labels` is a list of (key, title) pairs, used to describes the
        elements of the doughnut.
    - `link` is the link target.
    colors is an optional list of (color, highlight) pairs.

    `labels` specifies the order in which the values of counts are
    presented.

    Pairs in colors are repeated as needed if it does not
    contains enough entries.

    It is up to the caller to sanitize the parameters, if needed.
    """
    global _doughnut_cpt

    _doughnut_cpt += 1

    data = {
        'labels': [str(t) for (k, t) in labels],
        'datasets': [
            {
                'label': title,
                'data': [counts[k] for (k, t) in labels],
                'backgroundColor': [
                    i for i in (colors or DOUGHNUT_COLORS) * len(labels)
                ],
            }
        ],
    }
    return DOUGHNUT_TMPL.format(
        title=title,
        subtitle=subtitle,
        data=data,
        full=link,
        id="doughnut_%d" % _doughnut_cpt,
        legend=str(legend).lower(),
    )


_barchart_cpt = 0


def make_barchart(
    xaxis,
    datasets,
    colors=CHART_DATASET_COLORS,
    legend: bool = False,
    stacked: bool = False,
):
    """Return HTML-ready representation for barchart.

    - `xaxis` is a list of strings shown on horizontal axis, in order
    - `datasets` is an iterable of (title, data) pairs

    `title` is the dataset title, and `data` is a list of numerical
    values, in order.

    It is up to the caller to sanitize the parameters, if needed.
    """
    global _barchart_cpt

    _barchart_cpt += 1
    data = ",".join(
        DATASET_TMPL.format(title=title, data=data, c=c, h=h)
        for (title, data), (c, h) in zip(datasets, colors * len(datasets))
    )
    return BARCHART_TMPL.format(
        xaxis=xaxis,
        datasets=data,
        id="barchart_%d" % _barchart_cpt,
        legend=str(legend).lower(),
        stacked=str(stacked).lower(),
    )


_linechart_cpt = 0


def make_linechart(
    xaxis, datasets, colors=CHART_DATASET_COLORS, legend: bool = False
):
    """Return HTML-ready representation for linechart.

    - `xaxis` is a list of strings shown on horizontal axis, in order
    - `datasets` is an interable of (title, data) pairs

        `title` is the dataset title
        `data` is a list of numerical values, in order

    It is up to the caller to sanitize the parameters, if needed.
    """
    global _linechart_cpt

    _linechart_cpt += 1
    data = ",".join(
        DATASET_TMPL.format(title=title, data=data, c=c, h=h)
        for (title, data), (c, h) in zip(datasets, colors * len(datasets))
    )
    return LINECHART_TMPL.format(
        xaxis=xaxis,
        datasets=data,
        id="linechart_%d" % _linechart_cpt,
        legend=str(legend).lower(),
    )


def make_dialog(id, title, body, label=None):
    """Return HTML-ready representation for dialog.

    If `label` is not None, a 'submit' button is included.

    It is up to the caller to sanitize the parameters, if needed.
    """
    action_button = (
        ACTION_BUTTON_TMPL.format(id=id, label=label)
        if label is not None
        else ''
    )

    return DIALOG_TMPL.format(cancel=gettext('Cancel')).format(
        id=id, title=title, body=body, action_button=action_button
    )


def make_select(name, os, selected=0):
    """Return HTML-ready representation for select block.

    - `name` is the name/id of the select block.
    - `os` is a list of options.
    - `selected` is an optional number or a possibly empty collection of
        options.

    If `selected` is a collection, the options in `os` that are in
    `selected` will be selected, and the select block will allow multiple
    selections.

    If `selected` is a number, the item at that offset will be selected
    and the select block will be in single selection mode.

    If `selected` is not specified, the first item in `os` will be
    selected and the select block will be in single selection mode.

    The `os` option list will be sorted and the options added in order.
    """
    select = ' selected="selected"'
    single = isinstance(selected, (int))
    return '''<select name="{name}" id="{name}"{multi}>
                  {options}
              </select>'''.format(
        name=name,
        multi='' if single else ' multiple="multiple"',
        options='\n'.join(
            '<option{selected}>{o}</option>'.format(
                selected=select
                if (o == os[selected] if single else o in selected)
                else '',
                o=o,
            )
            for o in sorted(os)
        ),
    )


def make_venn5(sets, names=None, colors=VENN_COLORS):
    """Return HTML-ready representation for a Venn diagram.

    Only works nicely if the number of sets is 5.

    # Required parameters

    - `sets`: a dictionary.  Keys are strings and values are collections
        of hashable objects.

    # Optional parameters

    - `names`: an ordered collection of strings, which must be keys in
        `sets`.  If not provided, all `sets` keys, sorted, will be used.
    - `colors`: an iterable of strings (HTML colors). If not provided
        a default series of colors is provided.
    """

    def tag(prefix, iterable):
        return {prefix + str(i): v for i, v in enumerate(iterable, 1)}

    what = names or sorted(list(sets))
    cells = chain.from_iterable(
        combinations(what, 1 + r) for r in range(len(what))
    )
    items = {
        'd'
        + ''.join(map(lambda s: str(1 + what.index(s)), c)): len(
            reduce(set.intersection, [sets[s] for s in c])
            - reduce(set.union, [sets[s] for s in what if s not in c], set())
        )
        for c in cells
    }
    return VENN_TMPL.format(**items, **tag('n', what), **tag('c', colors))
