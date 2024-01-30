def add_stratigraphy_to_block_diagram(strat, prop, facies, dx, ve, xoffset, yoffset, scale, plot_surfs, color_mode, colors, colormap, vmin, vmax, line_thickness, export, opacity):
    """function for adding stratigraphy to the sides of a block diagram
    colors layers by relative age
    strat - input array with stratigraphic surfaces
    facies - 1D array of facies codes for layers
    h - channel depth (height of point bar)
    thalweg_z - array of thalweg elevations for each layer
    dx - size of gridcells in the horizontal direction in 'strat'
    ve - vertical exaggeration
    offset - offset in the y-direction relative to 0
    scale - scaling factor
    plot_surfs - if equals 1, stratigraphic boundaries will be plotted on the sides as black lines
    color_mode - determines what kind of plot is created; can be 'property', 'time', or 'facies'
    colors - colors scheme for facies (list of RGB values)
    line_thickness - tube radius for plotting layers on the sides
    export - if equals 1, the display can be saved as a VRML file for use in other programs (e.g., 3D printing)""" 
    r,c,ts=np.shape(strat)
    if color_mode == 'time':
        norm = matplotlib.colors.Normalize(vmin=0.0, vmax=ts-1)
        cmap = matplotlib.cm.get_cmap(colormap)
    if (color_mode == 'property') | (color_mode == 'facies'):
        norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
        cmap = matplotlib.cm.get_cmap(colormap)

    for layer_n in trange(ts-1): # main loop
        top = strat[:,0,layer_n+1]  # updip side
        base = strat[:,0,layer_n]
        if color_mode == "property":
            props = prop[:,0,layer_n]
        if plot_surfs:
            Y1 = scale*(yoffset + dx*np.arange(0,r))
            X1 = scale*(xoffset + np.zeros(np.shape(base)))
            Z1 = ve*scale*base
            mlab.plot3d(X1,Y1,Z1,color=(0,0,0),tube_radius=line_thickness)
        if np.max(top-base)>0:
            Points,Inds = triangulate_layers(top,base,dx)
            for i in range(len(Points)):
                vertices = Points[i]
                triangles, scalars = create_triangles(vertices)
                Y1 = scale*(yoffset + vertices[:,0])
                X1 = scale*(xoffset + dx*0*np.ones(np.shape(vertices[:,0])))
                Z1 = scale*vertices[:,1]
                if color_mode == "property":
                    scalars = props[Inds[i]]
                else:
                    scalars = []
                plot_layers_on_one_side(layer_n, facies, color_mode, colors, X1, Y1, Z1, ve, triangles, vertices, scalars, colormap, norm, vmin, vmax, export, opacity)

        top = strat[:,-1,layer_n+1]  # downdip side
        base = strat[:,-1,layer_n]
        if color_mode == "property":
            props = prop[:,-1,layer_n]
        if plot_surfs:
            Y1 = scale*(yoffset + dx*np.arange(0,r))
            X1 = scale*(xoffset + dx*(c-1)*np.ones(np.shape(base)))
            Z1 = ve*scale*base
            mlab.plot3d(X1,Y1,Z1,color=(0,0,0),tube_radius=line_thickness)
        if np.max(top-base)>0:
            Points,Inds = triangulate_layers(top,base,dx)
            for i in range(len(Points)):
                vertices = Points[i]
                triangles, scalars = create_triangles(vertices)
                Y1 = scale*(yoffset + vertices[:,0])
                X1 = scale*(xoffset + dx*(c-1)*np.ones(np.shape(vertices[:,0])))
                Z1 = scale*vertices[:,1]
                if color_mode == "property":
                    scalars = props[Inds[i]]
                else:
                    scalars = []
                plot_layers_on_one_side(layer_n, facies, color_mode, colors, X1, Y1, Z1, ve, triangles, vertices, scalars, colormap, norm, vmin, vmax, export, opacity)

        top = strat[0,:,layer_n+1]  # left edge (looking downdip)
        base = strat[0,:,layer_n]
        if color_mode == "property":
            props = prop[0,:,layer_n]
        if plot_surfs:
            Y1 = scale*(yoffset + np.zeros(np.shape(base)))
            X1 = scale*(xoffset + dx*np.arange(0,c))
            Z1 = ve*scale*base
            mlab.plot3d(X1,Y1,Z1,color=(0,0,0),tube_radius=line_thickness)
        if np.max(top-base)>0:
            Points,Inds = triangulate_layers(top,base,dx)
            for i in range(len(Points)):
                vertices = Points[i]
                triangles, scalars = create_triangles(vertices)
                Y1 = scale*(yoffset + dx*0*np.ones(np.shape(vertices[:,0])))
                X1 = scale*(xoffset + vertices[:,0])
                Z1 = scale*vertices[:,1]
                if color_mode == "property":
                    scalars = props[Inds[i]]
                else:
                    scalars = []
                plot_layers_on_one_side(layer_n, facies, color_mode, colors, X1, Y1, Z1, ve, triangles, vertices, scalars, colormap, norm, vmin, vmax, export, opacity)

        top = strat[-1,:,layer_n+1] # right edge (looking downdip)
        base = strat[-1,:,layer_n]
        if color_mode == "property":
            props = prop[-1,:,layer_n]
        if plot_surfs:
            Y1 = scale*(yoffset + dx*(r-1)*np.ones(np.shape(base)))
            X1 = scale*(xoffset + dx*np.arange(0,c))
            Z1 = ve*scale*base
            mlab.plot3d(X1,Y1,Z1,color=(0,0,0),tube_radius=line_thickness)
        if np.max(top-base)>0:
            Points,Inds = triangulate_layers(top,base,dx)
            for i in range(len(Points)):
                vertices = Points[i]
                triangles, scalars = create_triangles(vertices)
                Y1 = scale*(yoffset + dx*(r-1)*np.ones(np.shape(vertices[:,0])))
                X1 = scale*(xoffset + vertices[:,0])
                Z1 = scale*vertices[:,1]
                if color_mode == "property":
                    scalars = props[Inds[i]]
                else:
                    scalars = []
                plot_layers_on_one_side(layer_n, facies, color_mode, colors, X1, Y1, Z1, ve, triangles, vertices, scalars, colormap, norm, vmin, vmax, export, opacity)

def create_fence_diagram(strat, prop, facies, x0, y0, nx, ny, dx, ve, scale, plot_surfs, plot_sides, color_mode, colors, colormap, line_thickness, bottom, export, opacity):
    """function for creating a fence diagram
    inputs:
    strat - stack of stratigraphic surfaces
    facies - 1D array of facies codes for layers
    topo - stack of topographic surfaces
    nx - number of strike sections
    ny - number of dip sections
    dx - gridcell size
    ve - vertical exaggeration
    scale - scaling factor (for whole model)
    plot_surfs - if equals 1, the stratigraphic surfaces will be plotted on the sides (adds a lot of triangles - not good for 3D printing)
    color_mode - determines what kind of plot is created; can be 'property', 'time', or 'facies'
    colors - colors scheme for facies (list of RGB values)
    line_thickness - - tube radius for plotting layers on the sides
    bottom - elevation value for the bottom of the block
    export - if equals 1, the display can be saved as a VRML file for use in other programs (e.g., 3D printing)"""
    r,c,ts=np.shape(strat)
    gray = (0.6,0.6,0.6)
    norm = matplotlib.colors.Normalize(vmin=0.0, vmax=ts-1)
    cmap = matplotlib.cm.get_cmap(colormap)
    vmin = np.min(prop)
    vmax = np.max(prop)

    gray = (0.6,0.6,0.6) # color for plotting sides

    z = scale*strat[:,:,ts-1].T
    z1 = strat[:,:,0].T
    xoffset = 0; yoffset = 0
    
    # updip side:
    vertices, triangles = create_section(z1[:,0],dx,bottom) 
    x = scale*(xoffset + vertices[:,0])
    y = scale*(yoffset + np.zeros(np.shape(vertices[:,0])))
    z = scale*ve*vertices[:,1]
    mlab.triangular_mesh(x, y, z, triangles, color=gray, opacity = opacity)
    
    # downdip side:
    vertices, triangles = create_section(z1[:,-1],dx,bottom) 
    x = scale*(xoffset + vertices[:,0])
    y = scale*(yoffset + (r-1)*dx*np.ones(np.shape(vertices[:,0])))
    z = scale*ve*vertices[:,1]
    mlab.triangular_mesh(x, y, z, triangles, color=gray, opacity = opacity)

    # left edge (looking downdip):
    vertices, triangles = create_section(z1[0,:],dx,bottom) 
    x = scale*(xoffset + np.zeros(np.shape(vertices[:,0])))
    y = scale*(yoffset + vertices[:,0])
    z = scale*ve*vertices[:,1]
    mlab.triangular_mesh(x, y, z, triangles, color=gray, opacity = opacity)
    
    # right edge (looking downdip):
    vertices, triangles = create_section(z1[-1,:],dx,bottom) 
    x = scale*(xoffset + (c-1)*dx*np.ones(np.shape(vertices[:,0])))
    y = scale*(yoffset + vertices[:,0])
    z = scale*ve*vertices[:,1]
    mlab.triangular_mesh(x, y, z, triangles, color=gray, opacity = opacity)
    
    # bottom face of block:
    vertices = dx*np.array([[0,0],[c-1,0],[c-1,r-1],[0,r-1]])
    triangles = [[0,1,3],[1,3,2]]
    x = scale*(xoffset + vertices[:,0])
    y = scale*(yoffset + vertices[:,1])
    z = scale*bottom*np.ones(np.shape(vertices[:,0]))
    mlab.triangular_mesh(x, y, ve*z, triangles, color=gray, opacity = opacity)

    x_inds = np.hstack((0, int(c/(nx+1)) * np.arange(1, nx+1), c-1))
    for x1 in tqdm(x_inds): # strike sections
        if plot_sides:
            vertices, triangles = create_section(strat[:,x1,0],dx,bottom) 
            y = y0 + scale*(vertices[:,0])
            x = x0 + scale*(x1*dx+np.zeros(np.shape(vertices[:,0])))
            z = scale*ve*vertices[:,1]
            mlab.triangular_mesh(x,y,z,triangles,color=gray)
        for layer_n in range(ts-1): # main loop
            top = strat[:,x1,layer_n+1]  
            base = strat[:,x1,layer_n]
            if color_mode == 'property':
                props = prop[:,x1,layer_n]
            if plot_surfs:
                Y1 = y0 + scale*(dx*np.arange(0,r))
                X1 = x0 + scale*(x1*dx+np.zeros(np.shape(base)))
                Z1 = ve*scale*base
                mlab.plot3d(X1,Y1,Z1,color=(0,0,0),tube_radius=line_thickness)
            if np.max(top-base)>0:
                Points,Inds = triangulate_layers(top,base,dx)
                for i in range(len(Points)):
                    vertices = Points[i]
                    triangles, scalars = create_triangles(vertices)
                    Y1 = y0 + scale*(vertices[:,0])
                    X1 = x0 + scale*(x1*dx+dx*0*np.ones(np.shape(vertices[:,0])))
                    Z1 = scale*vertices[:,1]
                    if color_mode == 'property':
                        scalars = props[Inds[i]]
                    else:
                        scalars = []
                    plot_layers_on_one_side(layer_n, facies, color_mode, colors, X1, Y1, Z1, ve, triangles, vertices, scalars, colormap, norm, vmin, vmax, export, opacity)

    y_inds = np.hstack((0, int(r/(ny+1)) * np.arange(1, ny+1), r-1))
    for y1 in tqdm(y_inds): # dip sections
        if plot_sides:
            vertices, triangles = create_section(strat[y1,:,0],dx,bottom) 
            y = y0 + scale*(y1*dx+np.zeros(np.shape(vertices[:,0])))
            x = x0 + scale*(vertices[:,0])
            z = scale*ve*vertices[:,1]
            mlab.triangular_mesh(x,y,z,triangles,color=gray)
        for layer_n in range(ts-1): # main loop
            top = strat[y1,:,layer_n+1]  
            base = strat[y1,:,layer_n]
            if color_mode == 'property':
                props = prop[y1,:,layer_n]
            if plot_surfs:
                Y1 = y0 + scale*(y1*dx+np.zeros(np.shape(base)))
                X1 = x0 + scale*(dx*np.arange(0,c))
                Z1 = ve*scale*base
                mlab.plot3d(X1,Y1,Z1,color=(0,0,0),tube_radius=line_thickness)
            if np.max(top-base)>0:
                Points,Inds = triangulate_layers(top,base,dx)
                for i in range(len(Points)):
                    vertices = Points[i]
                    triangles, scalars = create_triangles(vertices)
                    Y1 = y0 + scale*(y1*dx + dx*0*np.ones(np.shape(vertices[:,0])))
                    X1 = x0 + scale*(vertices[:,0])
                    Z1 = scale*vertices[:,1]
                    if color_mode == 'property':
                        scalars = props[Inds[i]]
                    else:
                        scalars = []
                    plot_layers_on_one_side(layer_n, facies, color_mode, colors, X1, Y1, Z1, ve, triangles, vertices, scalars, colormap, norm, vmin, vmax, export, opacity)
        # print('done with section '+str(nsec)+' of '+str(ny)+' dip sections')
    r,c = np.shape(strat[:,:,-1])
    Y1 = scale*(np.linspace(0,r-1,r)*dx)
    X1 = scale*(np.linspace(0,c-1,c)*dx)
    topo_min = np.min(strat[:,:,-1])
    topo_max = np.max(strat[:,:,-1])
    mlab.surf(X1, Y1, scale*strat[:,:,-1].T, warp_scale=ve, colormap='gist_earth', vmin=scale*topo_min, vmax=scale*topo_max, opacity=0.15)