from unittest import TestCase

import pyvista as pv
import trimesh
from dreifus.pyvista import add_coordinate_axes
from famudy.data import FamudySequenceDataManager


class FamudySequenceDataManagerTest(TestCase):

    def test_load_NPHM(self):
        participant_id = 18
        sequence = "EXP-5-mouth"
        timestep = 33 * 3

        participant_id = 24
        sequence = "EXP-3-cheeks+nose"
        timestep = 9

        data_manager = FamudySequenceDataManager(participant_id, sequence)
        mesh = data_manager.load_NPHM_mesh(timestep, include_canonical_coordinates=True)
        canonical_coordinates = mesh.vertex_attributes['canonical_coordinates']

        canonical_mesh = trimesh.Trimesh(canonical_coordinates[..., :3], mesh.faces, process=False)

        p = pv.Plotter(shape=(1, 2))
        p.subplot(0, 0)
        p.add_mesh(canonical_mesh)
        # p.add_points(canonical_coordinates[..., :3])
        add_coordinate_axes(p, scale=0.1)

        p.subplot(0, 1)
        p.add_mesh(mesh)
        add_coordinate_axes(p, scale=0.1)
        p.link_views()
        p.show()
