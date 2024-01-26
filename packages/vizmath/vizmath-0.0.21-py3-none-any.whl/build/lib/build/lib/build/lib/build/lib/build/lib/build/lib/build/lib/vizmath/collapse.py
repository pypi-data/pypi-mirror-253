#%%
from quadtile_chart import quadtile as qt
from quadtile_chart import polyquadtile as pqt

#%%
qt_o = qt.random_quadtile(10)
qt_o.quadtile_plot()

# %%
df = qt_o.df.sort_values(by=['value'], ascending=True).head(200)
df['value'] = df['value']/1000
polygon = [(2,-2),(-2,2),(-7,-7),(7,7)]
pqt_o = pqt(df, 'id', 'value', 0, 0, buffer=0.1, rotate=0., constraints=polygon)
pqt_o.polyquadtile_plot(show_constraints=True)

#%%
# def __place_collapse(self, segments, segment, seg_idx, w, poly, lvl, lvl_h, collapse=False):
#     placed = False
#     # check the top side of the square to see if the points are within the polygon
#     top1 = vf.is_point_in_convex_polygon(segment.x, segment.y+w, poly)
#     top2 = vf.is_point_in_convex_polygon(segment.x+w, segment.y+w, poly)
#     # split the segment into 2 new ones after setting the square (or 1 new one if there's complete overlap)
#     if top1 and top2 and w <= segment.length and segment.y+w <= segment.height: # checking segment height for under-bridge segments
#         placed = True
#         if segment.y == lvl:
#             lvl_h = segment.y+w
        
#         # new code
#         x_seg = segment.x
#         w_seg = w
#         if collapse:
            
#             # find closest square from the left side and check if the new segment's y value happens to align with an existing closest segment
#             left_square = max((s for s in self.o_polysquares.viz if s.x+s.w <= segment.x and s.y <= segment.y+w and s.y+s.w >= segment.y+w), key=lambda s: s.x, default=None)
#             if left_square is not None:

#                 # set height for any affected segment, x endpoitns will be the same, closest y that's less than the segment y
#                 covered_segment = max((s for s in segments if s.x+s.length == segment.x and s.y < segment.y+w), key=lambda s: s.y, default=None)
#                 if covered_segment is not None:
#                     # set a new height for the covered segment
#                     covered_segment.height = segment.y+w 
                
#                 # check for existing segment at the y of the left square's top, if so merge with the segment
#                 merge_segment = max((s for s in segments if s.x+s.length <= segment.x and segment.y+w == s.y), key=lambda s: s.x, default=None)
                
#                 # check the top of the square, if matched, merge
#                 if merge_segment is not None: # potential merge
#                     if segment.y+w == left_square.y+left_square.w and left_square.x+left_square.w == merge_segment.x + merge_segment.length:
#                         if w == segment.length: # 1 segment (full overlap)
#                             segments[seg_idx] = self.__segment(merge_segment.x, segment.y+w, merge_segment.length+w, segment.height, False)
#                         else: # 2 segments
#                             segments[seg_idx:seg_idx+1] = [
#                                 self.__segment(merge_segment.x, segment.y+w, merge_segment.length+w, segment.height, False),
#                                 self.__segment(segment.x+w, segment.y, segment.length-w, segment.height, False)]
#                 else: # set the new positions
#                     x_seg = left_square.x
#                     w_seg += segment.x - x_seg
#         # end
        
#         # child segments shares the same height threshold as the parent in case the parent is an under-bridge segment
#         if w == segment.length: # 1 segment (full overlap)
#             segments[seg_idx] = self.__segment(x_seg, segment.y+w, w_seg, segment.height, False)
#         else: # 2 segments
#             segments[seg_idx:seg_idx+1] = [
#                 self.__segment(x_seg, segment.y+w, w_seg, segment.height, False),
#                 self.__segment(segment.x+w, segment.y, segment.length-w, segment.height, False)]
#     else:
#         if seg_idx is not None: 
#             segments[seg_idx].active = False
#     return placed, lvl_h