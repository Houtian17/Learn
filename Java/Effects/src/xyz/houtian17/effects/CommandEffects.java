package xyz.houtian17.effects;

import net.minecraft.server.v1_11_R1.EnumParticle;
import net.minecraft.server.v1_11_R1.PacketPlayOutWorldParticles;

import org.bukkit.Bukkit;
import org.bukkit.Effect;
import org.bukkit.Location;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.craftbukkit.v1_11_R1.entity.CraftPlayer;
import org.bukkit.entity.Player;

public class CommandEffects implements CommandExecutor {

    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        if (sender instanceof Player) {
            Player p = (Player) sender;
            if (args.length == 1) {
                if (args[0].equals("tp")) {
                    Location loc = p.getLocation();
                    p.getWorld().playEffect(loc, Effect.ENDER_SIGNAL, 0);
                    p.getWorld().playEffect(loc, Effect.ENDER_SIGNAL, 0);
                    p.getWorld().playEffect(loc, Effect.ENDER_SIGNAL, 0);
                }else if (args[0].equals("line")){
                    Location loc=p.getLocation();
                    float x=(float)loc.getX();
                    float y=(float)loc.getY();
                    float z=(float)loc.getZ();
                    for (int i=0;i<100;i++) {
                        PacketPlayOutWorldParticles packet = new PacketPlayOutWorldParticles(EnumParticle.FLAME, true, x, y, z, 0, 0, 0, 0, 1);
                        for (Player online : Bukkit.getOnlinePlayers()) {
                            ((CraftPlayer) online).getHandle().playerConnection.sendPacket(packet);
                        }
                        x=x+0.1f;
                    }
                }
            }
            return true;
        }
        return false;
    }
}
