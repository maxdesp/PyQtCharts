# -*- coding: utf-8 -*-

from qcharts import (PieChart, ScatterChart, LineChart, AreaChart,
                    DataTable, DialogViewer)
from PyQt5.Qt import QApplication,QSize
# from PyQt5.QtWidgets import 

def _pie_chart_demo():
    """ demonstration of pie chart
    """
    columns =['Lang', 'Rating']
    rows = [['Java', 17.874],
            ['C', 17.322],
            ['C++', 8.084],
            ['Python', 43.305],
            ['C#', 7.319],
            ['PHP', 6.096]]

    table = DataTable(columns, rows, key=1)
    # table.add_row()

    chart = PieChart(table)
    
    view = DialogViewer(size=(360, 240))
    view.set_graph(chart)
    view.exec_()

    # save dialog
    chart.save('', QSize(240, 240), 100)

    
def _scatter_chart_demo():
    """ demonstration of scatter chart
    """
    columns = ['Quality', 'Test 1', 'Test 2']
    rows = [[ 92,  4.9,  8.0],
            [ 94,  2.0,  2.5],
            [ 96,  7.2,  6.9],
            [ 98,  3.5,  1.2],
            [100,  8.0,  5.3],
            [102, 15.0, 14.2]]
    table = DataTable(columns, rows)
    
   
    chart = ScatterChart(table)
    chart.haxis_title = 'Process input'
    chart.haxis_vmin = 0
    chart.haxis_vmax = 16
    chart.haxis_step = 2
    chart.vaxis_title = 'Quality'
    chart.vaxis_vmin = 90
    chart.vaxis_vmax = 104
    chart.vaxis_step = 1

    #chart.save('scatter.png', QSize(400, 240), 100)

    view = DialogViewer()
    view.set_graph(chart)
    view.resize(400, 240)
    view.exec_()

def _line_chart_demo():
    """ demonstration of line chart
    """
    table = DataTable()
    table.add_column('Time')
    table.add_column('Site 1')
    table.add_column('Site 2')
    table.add_column('Site 3')
    table.add_row([ 4.00, 120,   80,  400])
    table.add_row([ 6.00, 270,  850,  320])
    table.add_row([ 8.30,  50, 1200,  280])
    table.add_row([10.15, 320, 1520,  510])
    table.add_row([12.00, 150,  930, 1100])
    table.add_row([18.20,  62, 1100,  240])

    chart = LineChart(table)
    chart.set_horizontal_axis_column(0)
    chart.haxis_title = 'Time'
    chart.haxis_vmin = 0.0
    chart.haxis_vmax = 20.0
    chart.haxis_step = 2

    #chart.save('line.png', QSize(400, 240), 100)

    view = DialogViewer()
    view.set_graph(chart)
    view.resize(400, 240)
    view.exec_()

def _area_chart_demo():
    """ demonstration of area chart
    """
    table = DataTable()
    table.add_column('Time')
    table.add_column('Site 1')
    table.add_column('Site 2')
    table.add_row([ 4.00, 120,   500])
    table.add_row([ 6.00, 270,   460])
    table.add_row([ 8.30, 1260, 1120])
    table.add_row([10.15, 2030,  540])
    table.add_row([12.00,  520,  890])
    table.add_row([18.20, 1862, 1500])

    chart = AreaChart(table)
    chart.set_horizontal_axis_column(0)
    chart.haxis_title = 'Time'
    chart.haxis_vmin = 0.0
    chart.haxis_vmax = 20.0
    chart.haxis_step = 5

    #chart.save('area.png', QSize(400, 240), 100)

    view = DialogViewer()
    view.set_graph(chart)
    view.resize(400, 240)
    view.exec_()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    _pie_chart_demo()
    _scatter_chart_demo()
    _line_chart_demo()
    _area_chart_demo()
