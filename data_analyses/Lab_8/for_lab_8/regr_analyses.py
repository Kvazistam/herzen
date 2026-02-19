def quality_assessment(solve_points, yv):
    n = len(yv)
    sum = 0
    for i in range(n):
        sum += (yv[i] - solve_points[i]) / yv[i]
    quality = sum / n
    return quality


def elasticity_coefficient(solve_points, xv, solve):
    b1 = solve[-1]
    med_x = sum(xv)/len(xv)
    med_y = sum(solve_points)/len(solve_points)
    elasticity = b1*med_y/med_x
    return elasticity

def student(xv, ):
    return 0