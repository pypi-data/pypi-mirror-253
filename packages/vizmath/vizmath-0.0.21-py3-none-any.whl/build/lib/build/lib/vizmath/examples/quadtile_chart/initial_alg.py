def polyquadtile_chart_example(self):

        #region initialize
        list_xy = dp()
        buffer = self.buffer
        # sort the values and calculate the width (including the buffer)
        df_sorted = self.df.sort_values(by=self.value_field, ascending=False)
        df_sorted['width'] = (df_sorted[self.value_field].apply(sqrt)) + buffer * 2
        df_center = df_sorted.iloc[0:1] # first record
        df_quad = df_sorted.iloc[1:] # quad records
        # calculate the length of the first segment between the origin and the polygon boundary
        center_w = df_center['width'].values[0]
        offset = center_w/2. # offset by the half-width
        poly_quad = self.__quad_vertices(offset)
        # center details
        center_id = df_center[self.id_field].values[0]
        center_a = df_center[self.value_field].values[0]
        # retrieve values for looping
        widths = df_quad['width'].values
        ids = df_quad[self.id_field].values
        areas = df_quad[self.value_field].values
        self.__add_square(list_xy, 0, center_id, 0., 0., center_w, center_a, 'center')
        #endregion

        # top example
        poly = poly_quad['top']
        length = self.__seg_len_to_ploy(0., 0., poly)
        segments = []
        segments.append(self.__segment(0., 0., length=length)) # first segment
        
        #region algorithm
        lvl = 0.
        lvl_h = 0.
        i = 0
        while i < len(widths):

            w = widths[i]
            id = ids[i]
            a = areas[i]
            # get the last segment/bridge at the end of the line
            last_lvl_segment = max((s for s in segments if s.y == lvl), key=lambda s: s.x)

            # segments sorted by smallest height (for bridge segments) then smallest x that are active
            sorted_segments = copy.deepcopy(sorted([s for s in segments if s.active], key=lambda s: (s.height, s.x)))
            p = 0 # check how many were placed
            for j in range(len(sorted_segments)):
                
                segment = sorted_segments[j]
                seg_idx = next((i for i, s in enumerate(segments) if s == segment), None)
                placed, lvl_h = self.__place(segments, segment, seg_idx, w, poly, lvl, lvl_h) # place square if possible

                if segment == last_lvl_segment and not placed and lvl != lvl_h: # create a bridge segment
                    last_lvl_segment.height = lvl_h # set a threshold for the under-bridge segment
                    lvl = lvl_h # reset the level
                    # check if a segment exists at the lvl_h, if so, extend it, otherwise create a new one
                    lvl_h_seg = max((s for s in segments if s.y == lvl_h), key=lambda s: s.x, default=None)
                    if lvl_h_seg is not None: # extend it
                        lvl_h_seg.length += self.__seg_len_to_ploy(lvl_h_seg.x, lvl_h, poly)
                    else: # create new
                        segments.append(self.__segment(segment.x, lvl_h, length=self.__seg_len_to_ploy(segment.x, lvl_h, poly)))
                    [setattr(s, 'active', True) for s in segments]
                    break
                elif placed:
                    # add square
                    self.__add_square(list_xy, i+1, id, segment.x, segment.y, w, a, 'top')
                    if j+1 == len(sorted_segments): # last segment
                        [setattr(s, 'active', True) for s in segments]
                    i += 1
                    break
                else:
                    if j+1 == len(sorted_segments): # last segment reached so add more bridges if possible:
                        # if (x,y) of the last_lvl_segment match the lower right corner of an existing square
                        #   then add another bridge at the top right corner of that square
                        #   (or extend a segment if one is already there)
                        upper_square = next((s for s in self.o_polysquares.viz if s.x +s.w == last_lvl_segment.x and s.y == last_lvl_segment.y), None)
                        if upper_square is not None:
                            # set height restriction on old bridge
                            last_lvl_segment.height = upper_square.w
                            lvl += upper_square.w
                            lvl_h = lvl
                            # check if a segment exists at the lvl_h, if so, extend it, otherwise create a new one
                            lvl_h_seg = max((s for s in segments if s.y == lvl), key=lambda s: s.x, default=None)
                            if lvl_h_seg is not None: # extend it
                                lvl_h_seg.length += self.__seg_len_to_ploy(lvl_h_seg.x, lvl, poly)
                            else: # create new
                                usx = upper_square.x + upper_square.w
                                segments.append(self.__segment(usx, lvl, length=self.__seg_len_to_ploy(usx, lvl, poly)))
                            [setattr(s, 'active', True) for s in segments]
                            break
                        i = len(widths) # no segments work
        #endregion

        #region rotate
        path_counter = 1
        for o in sorted(list_xy.viz, key=lambda o: (o.item, o.path)):
            if path_counter == 6:
                path_counter = 1
            if path_counter == 1 or path_counter == 5:
                o.x += buffer
                o.y += buffer
            if path_counter == 2:
                o.x += buffer
                o.y -= buffer
            if path_counter == 3:
                o.x -= buffer
                o.y -= buffer
            if path_counter == 4:
                o.x -= buffer
                o.y += buffer
            revert = 0.
            if o.side == 'center':
                revert_x = offset
                revert_y = offset
            if o.side == 'top':
                revert_x = offset
                revert_y = -offset
            xa, ya = vf.rotate(o.x, o.y, self.rotate, revert_x, revert_y)
            o.x = xa+self.xo
            o.y = ya+self.yo
            path_counter += 1
        #endregion

        self.o_polyquadtile_chart = list_xy
        self.o_polyquadtile_chart.to_dataframe()
